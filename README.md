## Hi, I'm Helen 👋

Backend engineer, mostly Java and Go, mostly payments. The last few years I've been on the issuing side of card
payments: authorization, tokenization, 3DS2, scheme integrations (Visa, Mastercard, UnionPay), settlement and
reconciliation. Before that I was at Adobe on Workfront and Fusion, splitting a monolith into services and building
connectors for things like Outlook, Salesforce and Jira.

Open to remote B2B work. More on [helenarams.github.io](https://helenarams.github.io) or
[LinkedIn](https://www.linkedin.com/in/helen-aramyan/).

### Things I've put here

Small projects I built to scratch an itch, or to try an idea properly instead of in a work branch.
Nothing here comes from employer code, and every card number is a scheme test range.

- **[card-auth-simulator](https://github.com/HelenArams/card-auth-simulator)** – a tiny issuer: rules pipeline, ISO 8583 response codes, holds, velocity limits. Java 17, Spring Boot.
- **[iso8583-go](https://github.com/HelenArams/iso8583-go)** – pack and unpack ISO 8583 messages with zero dependencies. Mostly because I wanted to understand bitmaps properly.
- **[settlement-recon-cli](https://github.com/HelenArams/settlement-recon-cli)** – matches authorizations against clearing records, with the tolerances and edge cases that break month-end.
- **[payment-webhooks](https://github.com/HelenArams/payment-webhooks)** – signed webhooks with retries and a dead-letter queue. Spring Boot.
- **[idempotency-spring-starter](https://github.com/HelenArams/idempotency-spring-starter)** – `@Idempotent` on a controller method so client retries don't double-charge. In-memory or Redis.
- **[decline-code-assistant](https://github.com/HelenArams/decline-code-assistant)** – a LangGraph agent on Claude that explains why transactions declined, with citations into a curated knowledge base. Also runs as an MCP server.
- **[fraud-triage-agent](https://github.com/HelenArams/fraud-triage-agent)** – LangGraph agent for the grey zone of card fraud: rule features score it, Claude (Anthropic API or Bedrock) investigates with tools, guardrails check the verdict, and high-risk cases pause for a human.
- **[luhn-bin-kit](https://github.com/HelenArams/luhn-bin-kit)** – Luhn, BIN detection, PAN masking. Small, but I reach for it constantly.

Older: [influxdb-pytest-plugin](https://github.com/HelenArams/influxdb-pytest-plugin), from my test-automation days.

### Lately

Agentic tooling for payment operations: LangGraph graphs, MCP servers, retrieval over curated runbooks, and evals so
the model has to earn its answers. Also strong opinions on when Go beats Java in a payments stack, happy to argue.

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=HelenArams&layout=compact&hide_border=true&hide=html,css,javascript,jupyter%20notebook" alt="languages" height="150">
