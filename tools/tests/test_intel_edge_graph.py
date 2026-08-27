"""Rigor checks for INTEL_EDGE_GRAPH_V0_1 empty scaffold.

No jsonschema dependency: these tests lock the FAMILY membrane and promotion
gate so the empty lab cannot silently grow family binds or fake-green edges.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

PLUGIN_DIR = (
    Path(__file__).resolve().parent.parent.parent
    / "plugins"
    / "intel-edge-graph"
    / "skills"
    / "intel-edge-graph"
    / "references"
)
EMPTY_PATH = PLUGIN_DIR / "INTEL_EDGE_GRAPH_EMPTY_V0_1.json"
SCHEMA_PATH = PLUGIN_DIR / "INTEL_EDGE_GRAPH_V0_1.schema.json"

_SHA256 = re.compile(r"^[a-f0-9]{64}$")
_INTEL_ID = re.compile(r"^INTEL_[A-Z0-9_]+$")
_INTEL_EDGE_ID = re.compile(r"^INTEL_EDGE_[A-Z0-9_]+$")
_UNVERIFIABLE_EVIDENCE = frozenset({"ANONYMOUS_SOURCE", "PRESS_SUMMARY"})
_FAMILY_IDS = frozenset(
    {
        "DADDY_JAY",
        "MRS_WISDOM",
        "MARYDEE",
        "LEANNE",
        "GAGA",
        "GRAMMY",
        "JAYCEE",
        "HEIDEE",
        "BRIANNA",
        "BE",
        "BRE",
        "AUNT_RANN",
        "AUNT_MAY",
        "UNCLE_DEE",
    }
)


def _load_empty() -> dict:
    return json.loads(EMPTY_PATH.read_text(encoding="utf-8"))


def _verified_allowed(edge: dict) -> bool:
    """Mirror the schema promotion gate without jsonschema."""
    if edge.get("status") != "VERIFIED":
        return True
    evidence = edge.get("evidence") or {}
    digest = evidence.get("receipt_sha256")
    if not isinstance(digest, str) or not _SHA256.fullmatch(digest):
        return False
    if not evidence.get("source_ref"):
        return False
    if evidence.get("evidence_type") in _UNVERIFIABLE_EVIDENCE:
        return False
    if edge.get("predicate") == "ATTRIBUTES_MOTIVE":
        return False
    return edge.get("origin") in {"DOCUMENT_SOURCE_BOUND", "ON_RECORD_QUOTE_BOUND"}


def test_empty_instance_locked_invariants() -> None:
    graph = _load_empty()
    assert graph["classification"] == "INTEL_STORY_GRAPH"
    assert graph["family_bind"] is False
    assert graph["nodes"] == []
    assert graph["edges"] == []
    invariants = graph["invariants"]
    assert invariants["authority_created"] is False
    assert invariants["facts_promoted"] == 0
    assert invariants["edges_inferred"] == 0
    assert invariants["silent_inference"] == "BLOCKED"
    assert invariants["family_bind"] is False


def test_empty_instance_forbids_family_ids() -> None:
    graph = _load_empty()
    forbidden = set(graph["forbidden_node_ids"])
    assert forbidden >= _FAMILY_IDS
    for node in graph["nodes"]:
        assert node["node_id"] not in forbidden
        assert _INTEL_ID.fullmatch(node["node_id"])


def test_schema_file_present_and_named() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    assert schema["title"] == "INTEL_EDGE_GRAPH_V0_1"
    assert schema["properties"]["family_bind"]["const"] is False
    assert schema["$defs"]["invariants"]["properties"]["edges_inferred"]["const"] == 0
    assert schema["$defs"]["invariants"]["properties"]["silent_inference"]["const"] == "BLOCKED"


def test_verified_without_hash_is_rejected() -> None:
    edge = {
        "edge_id": "INTEL_EDGE_001",
        "source_node": "INTEL_OUTLET_EXAMPLE",
        "target_node": "INTEL_OFFICIAL_EXAMPLE",
        "predicate": "CLAIMS",
        "origin": "USER_DECLARED",
        "evidence": {"evidence_type": "PRESS_SUMMARY"},
        "status": "VERIFIED",
    }
    assert _INTEL_EDGE_ID.fullmatch(edge["edge_id"])
    assert _verified_allowed(edge) is False


def test_anonymous_source_cannot_verify() -> None:
    edge = {
        "status": "VERIFIED",
        "predicate": "REPORTS",
        "origin": "DOCUMENT_SOURCE_BOUND",
        "evidence": {
            "evidence_type": "ANONYMOUS_SOURCE",
            "source_ref": "https://example.invalid/story",
            "receipt_sha256": "a" * 64,
        },
    }
    assert _verified_allowed(edge) is False


def test_motive_cannot_verify() -> None:
    edge = {
        "status": "VERIFIED",
        "predicate": "ATTRIBUTES_MOTIVE",
        "origin": "ON_RECORD_QUOTE_BOUND",
        "evidence": {
            "evidence_type": "ON_RECORD_QUOTE",
            "source_ref": "https://example.invalid/quote",
            "receipt_sha256": "b" * 64,
        },
    }
    assert _verified_allowed(edge) is False


def test_declared_without_hash_is_allowed() -> None:
    edge = {
        "status": "DECLARED",
        "predicate": "CLAIMS",
        "origin": "USER_DECLARED",
        "evidence": {"evidence_type": "PRESS_SUMMARY"},
    }
    assert _verified_allowed(edge) is True
