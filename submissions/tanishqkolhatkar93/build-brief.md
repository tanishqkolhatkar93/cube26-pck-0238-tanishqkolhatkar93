# Build Brief

**Project:** Pack Manager AI
**Goal:** Build a robust, fail-safe vision agent to verify outbound warehouse packages against expected order manifests.

**Key Requirements:**
- Must handle Multi-Tenant isolation (3PLs).
- Must emit a strictly formatted Evidence Contract (JSON + SHA256 hashing).
- Must Fail-Open gracefully on API errors.
- Must evaluate to `SEAL`, `STOP_AND_FIX`, or `UNCERTAIN`.