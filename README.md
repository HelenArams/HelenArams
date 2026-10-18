<h1 align="center">Hi, I'm Helen Aramyan 👋</h1>

<p align="center">
  <b>Senior Java &amp; Go Backend Engineer · Team Lead · Fintech &amp; Card Payments · AI Engineering</b><br/>
  Frankfurt, Germany · Open to remote B2B contracts
</p>

<p align="center">
  <a href="https://helenarams.github.io"><img alt="Website" src="https://img.shields.io/badge/helenarams.github.io-portfolio-0A66C2?style=flat-square&logo=googlechrome&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/helen-golang-java-ai-engineer/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-connect-0A66C2?style=flat-square&logo=linkedin"></a>
  <a href="mailto:helen.aramyan@gmail.com"><img alt="Email" src="https://img.shields.io/badge/email-helen.aramyan%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white"></a>
</p>

---

### What I do

I build the backend of card payments: authorization, tokenization, 3DS2, settlement and reconciliation.
Ten-plus years in Java, the last several also in Go, currently leading backend engineering at a licensed
digital bank. Before that I was at Adobe (Workfront, Fusion) splitting monoliths into microservices and
building enterprise integrations.

Lately I also build agentic tooling for payments operations with LLMs: LangGraph graphs, MCP servers,
retrieval over curated knowledge bases, and evals that keep them honest.

### Featured projects

| Project | Stack | What it shows |
|---|---|---|
| [card-auth-simulator](https://github.com/HelenArams/card-auth-simulator) | Java 17 · Spring Boot | Issuer-side authorization rules engine with ISO 8583 response codes, holds, velocity limits, idempotent replays |
| [iso8583-go](https://github.com/HelenArams/iso8583-go) | Go · stdlib only | Dependency-free ISO 8583 packer/unpacker with bitmaps, LLVAR/LLLVAR fields, and a demo auth switch |
| [settlement-recon-cli](https://github.com/HelenArams/settlement-recon-cli) | Go · Cobra | Tiered matching of authorizations against clearing records: tolerances, late presentments, duplicates |
| [payment-webhooks](https://github.com/HelenArams/payment-webhooks) | Java 17 · Spring Boot | Signed, at-least-once payment webhooks with backoff, dead-letter queue and replay |
| [idempotency-spring-starter](https://github.com/HelenArams/idempotency-spring-starter) | Java · Spring Boot starter | `@Idempotent` for REST endpoints: fingerprinted keys, in-memory and Redis stores |
| [decline-code-assistant](https://github.com/HelenArams/decline-code-assistant) | Python · LangGraph · Anthropic API · MCP | Agent that explains card declines from a CSV, grounded in a curated knowledge base, exposed as an MCP server |

Smaller utilities: [luhn-bin-kit](https://github.com/HelenArams/luhn-bin-kit) (Luhn, BIN detection, PAN masking)
· [influxdb-pytest-plugin](https://github.com/HelenArams/influxdb-pytest-plugin) (pytest results to InfluxDB).

### Stack

<p>
  <img alt="Java" src="https://img.shields.io/badge/Java-17%2B-ED8B00?style=flat-square&logo=openjdk&logoColor=white">
  <img alt="Spring Boot" src="https://img.shields.io/badge/Spring_Boot-3-6DB33F?style=flat-square&logo=springboot&logoColor=white">
  <img alt="Go" src="https://img.shields.io/badge/Go-1.2x-00ADD8?style=flat-square&logo=go&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Kafka" src="https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white">
  <img alt="Redis" src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white">
  <img alt="AWS" src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws">
  <img alt="GCP" src="https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white">
  <img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white">
  <img alt="Terraform" src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white">
  <img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white">
  <img alt="MCP" src="https://img.shields.io/badge/MCP-servers-000000?style=flat-square">
</p>

**Payments:** Visa (VTS, Visa Direct) · Mastercard (MDES, Send) · MPGS · UnionPay · 3DS2 · tokenization · PCI DSS · settlement and reconciliation · core banking integration

**Architecture:** DDD · CQRS · event-driven · sagas and outbox · hexagonal services · REST and gRPC

### GitHub

<p>
  <img src="https://github-readme-stats.vercel.app/api?username=HelenArams&show_icons=true&hide_border=true&theme=default&hide=stars" alt="GitHub stats" height="160">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=HelenArams&layout=compact&hide_border=true&hide=html,css,javascript,jupyter%20notebook" alt="Top languages" height="160">
</p>

<sub>All sample card numbers in these repositories are scheme test ranges. Nothing here is derived from employer code.</sub>
