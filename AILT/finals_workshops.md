# AILT Final Project — Workshop Schedule

Workshops aligned to the five milestones of the COMP 395-1 Final Project: *Design, Build, Optimize, and Ship a Novel AI-Powered Learning Technology*.

## Summary Timeline

| Week | Dates | Milestone | Workshops |
|------|-------|-----------|-----------|
| 6 | 3/9–3/13 | Pre-M1 | 1 (Learning theories), 2 (AI modalities + APIs), 3 (Prompt optimization preview) |
| 7 | 3/15–3/20 | **M1 due** | Teams work on proposals; office hours |
| 8 | 3/22–3/27 | **M2 due** | 4 (Cloud API in Flask), 5 (VLM/STT/TTS), 6 (Wireframing) |
| 9 | 3/29–4/4 | **M3 due** | 7 (Prompt optimization hands-on), 8 (DSPy, optional), 9 (User testing protocol) |
| 10 | 4/6–4/10 | **M4 due** | 10 (Productionization concepts) |
| 11 | 4/14–4/18 | Pre-M5 | 11 (Demo prep + writing) |
| 12 | 4/20–4/28 | **M5 due** | Demos + report |

---

## Before/During M1 — by ~3/14 (proposals due 3/15–3/20)

### Workshop 1: Learning Theories for Design
**Priority: high** | ~50 min

Students have behaviorism and a touch of constructionism from Labs 3–4. M1 requires them to *name a theory and map it to 3+ specific app features*. They need broader exposure.

**Topics:**
- Cognitivism (schema theory, cognitive load theory, worked examples)
- Constructivism (Vygotsky, ZPD, scaffolding)
- Constructionism (Papert — building to learn)
- Socratic method as a design pattern
- How to go from "I like constructivism" to "here are 3 specific app behaviors that instantiate it"

**Activity:** Given a sample app idea (e.g., a math tutor), small groups each take a different theory and sketch how it would change the app's behavior. Compare results.

---

### Workshop 2: AI Modalities Overview + Cloud API Setup
**Priority: high** | ~50 min

Students have only used local Ollama + LiteLLM. M1 requires a *modality justification* and *cost/privacy analysis*.

**Topics:**
- Cloud API landscape: OpenAI, Anthropic, Google — pricing tiers, model sizes, when to use which
- VLMs: what they are, how image input works (base64, multipart), example API calls
- STT/TTS: Whisper API, browser Web Speech API, ElevenLabs — quick demos
- Setting hard spend limits (screenshot it!) and `.env` / `.env.example` pattern
- Cost estimation: "If your app makes X calls/day at Y tokens each..."

**Activity:** Cost estimation exercise — given a usage scenario, calculate monthly cost across 3 different model tiers. Discuss where the cost/capability tradeoff sits for a tutoring app.

---

### Workshop 3: Prompt Optimization Methods Preview
**Priority: medium** | ~30–45 min

M1 requires students to *choose* a prompt optimization method and *define evaluation criteria before writing any prompts*.

**Topics:**
- Overview of all 3 options (A/B testing, iterative refinement, DSPy)
- What makes a good evaluation rubric with behavioral anchors
- How to write a test scenario set (happy paths, misconceptions, edge cases, adversarial)
- Matching optimization method to project type

**Activity:** Draft 3–5 sample rubric criteria for a hypothetical tutor (e.g., "When a student gives a wrong answer, the tutor should ___"). Practice writing behavioral anchors at each score level.

---

## Before/During M2 — by ~3/22 (walking skeleton due 3/23–3/27)

### Workshop 4: Cloud API Integration in Flask
**Priority: high** | ~50 min

The biggest technical gap. Students know Flask + LiteLLM + Ollama. Now they need to call cloud APIs.

**Topics:**
- OpenAI / Anthropic / Google Python SDK basics — `pip install openai anthropic google-generativeai`
- Swapping LiteLLM calls for direct SDK calls (or using LiteLLM with cloud providers)
- Handling API keys via `os.environ` and `python-dotenv`
- Error handling for API failures (rate limits, timeouts, 500s) — the spec explicitly requires graceful errors
- `.env.example` pattern for team collaboration

**Activity:** Live coding — take the Lab 4 conversational tutor and swap the Ollama backend for GPT-4o-mini or Claude Haiku. Students follow along and get it running on their machines.

---

### Workshop 5: VLM / STT / TTS Integration
**Priority: medium-high** | ~45 min (choose-your-own-adventure format)

Only needed by teams choosing these modalities, but likely several will.

**VLM track (~30 min):**
- Image upload in Flask (HTML file input, reading as base64)
- Sending images to OpenAI / Anthropic / Gemini vision APIs
- Handling the response and displaying results

**STT track (~30 min):**
- Browser Web Speech API (JS-side, no server needed)
- Server-side Whisper via OpenAI API
- Sending transcribed text to the LLM pipeline

**TTS track (~20 min):**
- Browser `speechSynthesis` API (simplest, free)
- Server-side TTS APIs (OpenAI TTS, ElevenLabs)

**Format:** Students attend the track they need. Each track has a minimal working example they can adapt.

---

### Workshop 6: Wireframing and the Walking Skeleton Pattern
**Priority: low-medium** | ~20 min

**Topics:**
- What "walking skeleton" means — thinnest end-to-end slice, ugly is fine
- Quick wireframing (Figma or paper) to plan UI before coding
- Project directory structure for the final project (`prompts/`, `data/`, `tests/`, `docs/`)
- The "is it a product or a wrapper?" gut-check from the spec

**Activity:** Each team sketches their walking skeleton on paper — what is the minimum user journey from open-browser to LLM-response? Identify the single riskiest technical piece and plan to build that first.

---

## Before/During M3 — by ~3/29 (optimization report due 3/30–4/4)

### Workshop 7: Systematic Prompt Optimization
**Priority: high** | ~50 min

The "intellectual core" of the project per the spec. Students need hands-on practice with the methodology, not just a description.

**Topics:**
- Running a structured evaluation: take a prompt, run 15 scenarios, score with a rubric
- LLM-as-judge: writing a judge prompt, automating scoring with a short script
- Version control for prompts (`prompts/v0.txt` -> `v1.txt` with `CHANGELOG.md`)
- Hypothesis-driven iteration: "I believe X will improve Y because Z"
- Regression awareness: when fixing one behavior breaks another

**Activity:** Everyone gets the same bad system prompt + 5 test cases. Score the baseline, write a hypothesis, revise the prompt, re-score. Compare results across pairs. Full iteration cycle in ~25 min.

---

### Workshop 8: DSPy Quickstart (Optional)
**Priority: low** | ~30 min or async tutorial

Only for teams choosing Option C.

**Topics:**
- `pip install dspy-ai`, configure with their provider
- BootstrapFewShot walkthrough on a toy example
- Writing a `metric(gold, pred)` function
- Reading and interpreting the optimization trace

**Format:** Could be office hours or a self-paced tutorial doc rather than a full class session.

---

### Workshop 9: User Testing Protocol Design
**Priority: medium** | ~30 min

M3 requires the testing *protocol* submitted and at least one session conducted.

**Topics:**
- Think-aloud method: what it is, how to facilitate without leading
- Writing a task script (2–3 tasks, consistent across participants)
- Exit questionnaire design (perceived helpfulness, confusion points, one change)
- Ethics: informed consent, anonymization, adults only (18+)

**Activity:** Role-play — pairs take turns as "user" and "facilitator" on a sample app. Practice think-aloud facilitation for 5 minutes, then debrief on what was hard about not leading the user.

---

## Before/During M4 — by ~4/5 (user testing + productionization due 4/6–4/10)

### Workshop 10: Productionization Concepts
**Priority: high** | ~50 min

Students have zero deployment experience. This is genuinely new content.

**Topics:**
- Docker basics: what a container is, Dockerfile structure (conceptual — no need to actually deploy)
- Deployment platforms: Render, Railway, Fly.io — show a quick walkthrough
- Serverless alternative: Lambda + API Gateway (conceptual overview)
- Cost modeling: "Your app uses GPT-4o-mini at ~$0.15/1M input tokens. With 100 DAU making 20 calls each at 500 tokens..."
- Data privacy: FERPA basics, student data retention policies, cloud vs. local tradeoffs
- Failure modes: API down, model hallucinates, student inputs something harmful

**Activity:** Cost modeling exercise — each team estimates their app's monthly cost at 100 DAU and 1,000 DAU. Discuss: at what point does this become unsustainable? What levers do you have?

---

## Before M5 — by ~4/18 (demos 4/20–4/28)

### Workshop 11: Demo Prep and Technical Writing
**Priority: low-medium** | ~20–30 min

**Topics:**
- Demo structure walkthrough (the spec gives a 12-min breakdown: Problem & Theory 2 min, Live Demo 6 min, Optimization Story 2 min, User Testing 1 min, Reflection 1 min)
- Tips: have the app running before your slot, prepare a "golden path" scenario, have a backup plan if the API is slow
- Report structure review: prose not bullets, all 8 sections, honest reflection matters
- Common pitfalls: "we used constructivism" without specifics, optimization section that reads as a changelog without analysis

**Activity:** Peer rehearsal — teams practice their 2-min "Problem & Theory" pitch with another team. Get feedback on clarity and whether the theory connection is specific enough.

---

## Notes

- **Heaviest weeks:** Week 6 (3 workshops before M1) and Week 8 (technical integration before M2). Week 6 is the most critical — if students lack theory vocabulary and API literacy before proposals, M1 will be weak and everything downstream suffers.
- **Workshop 5** (VLM/STT/TTS) could be split across office hours if class time is tight, since not all teams need all tracks.
- **Workshop 8** (DSPy) is optional and could be an async resource rather than class time.
- Several workshops include activities designed as think-pair-share or small-group exercises, consistent with the course's cognitivist/constructivist pedagogy.
