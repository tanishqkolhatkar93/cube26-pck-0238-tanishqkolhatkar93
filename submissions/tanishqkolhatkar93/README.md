# Pack Manager AI

## Overview
Pack Manager AI is a vision-based warehouse automation agent designed to verify outbound packages before they are sealed. By comparing an image of the open box against the expected order lines, it ensures that no items are missing, incorrect, or wrongly quantified.

If anything is wrong, it issues a `STOP & FIX` command. If all is correct, it issues a `SEAL` command.

## Solution Architecture
- **Frontend**: Streamlit (app.py) for an operator-hand-held tablet experience.
- **Backend**: FastAPI (uvicorn) handling concurrent image processing and Cryptographic Evidence Contracts.
- **AI Layer**: Google Gemini Flash Lite, using Structured Outputs (Pydantic) to convert vision into strict boolean matching logic.

## Setup
1. Navigate to `submissions/tanishqKolhatkar93/agents`.
2. Add your Google API Key to `.env`.
3. Start the backend: `uvicorn main:app --reload --env-file .env`
4. Open a new terminal, navigate to `app.py` and run the frontend: `streamlit run app.py`

## Assumptions &amp; Limitations
- __No Scale Reference__: If two products share the exact same packaging but different sizes, the AJ may not be able to distinguish them without a scale reference in the box.
- __Overlapping Soft-Goods__: Multiple folded t-shirts of the same color can sometimes be undercounted if they are perfectly stacked.
- __TENANCY ISOLATION__: The system assumes it is operating in a 3PL environment; thus, all AJ requests and database writes are secured by an `org_id` rowlevel security model.