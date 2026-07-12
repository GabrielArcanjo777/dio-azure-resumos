# Tipos de Serviço de Nuvem na Azure

## Modelo de responsabilidade compartilhada

Na computação em nuvem, provedor e cliente dividem responsabilidades. A Microsoft sempre protege a infraestrutura física da nuvem, mas a parcela administrada pelo cliente varia conforme o modelo contratado. Quanto mais gerenciado for o serviço, menor é o esforço com infraestrutura e maior é o foco nos dados e na aplicação.

Identidade, controle de acesso, classificação dos dados e configuração correta dos recursos continuam exigindo participação do cliente em todos os modelos.

## IaaS — Infraestrutura como Serviço

Em **IaaS**, o provedor entrega recursos de infraestrutura virtualizados, como máquinas, discos e redes. O cliente controla o sistema operacional, as atualizações, os componentes instalados, as aplicações e os dados.

**Exemplo no Azure:** Máquinas Virtuais do Azure.

**Quando usar:** migrações com poucas alterações, aplicações legadas ou cenários que exigem acesso e configuração do sistema operacional.

## PaaS — Plataforma como Serviço

Em **PaaS**, o provedor também administra sistema operacional, middleware, runtime, correções e parte da escalabilidade. O cliente concentra-se no código, na configuração da aplicação e nos dados.

**Exemplos no Azure:** Serviço de Aplicativo do Azure, Banco de Dados SQL do Azure e Azure Functions.

**Quando usar:** desenvolvimento e publicação rápida de aplicações sem administrar servidores diretamente.

## SaaS — Software como Serviço

Em **SaaS**, o provedor entrega uma aplicação completa pela internet e administra praticamente toda a pilha técnica. O cliente configura o uso do produto, gerencia usuários, acessos e os dados inseridos na solução.

**Exemplos:** Microsoft 365, Dynamics 365 e outras aplicações prontas consumidas por assinatura.

**Quando usar:** quando a necessidade pode ser atendida por um produto pronto, sem desenvolver ou manter a plataforma subjacente.

## Comparação dos modelos

| Modelo | Cliente administra principalmente | Maior benefício | Maior atenção |
|---|---|---|---|
| IaaS | Sistema operacional, aplicações e dados | Controle e flexibilidade | Operação e manutenção |
| PaaS | Aplicações, configurações e dados | Produtividade e agilidade | Limites e características da plataforma |
| SaaS | Usuários, acessos, configurações e dados | Uso imediato | Governança e adequação do produto |

Modelos de serviço não devem ser confundidos com modelos de implantação — nuvem pública, privada e híbrida — que descrevem onde e de que forma os recursos são disponibilizados.

## Como escolher

A decisão deve considerar o nível de controle necessário, competências da equipe, velocidade de entrega, requisitos de portabilidade, conformidade, disponibilidade e custo total de operação. Uma mesma arquitetura pode combinar os três modelos: por exemplo, SaaS para colaboração, PaaS para uma API e IaaS para um componente legado.

## Insights/Aprendizados

- IaaS oferece mais controle, mas exige mais administração do cliente.
- PaaS reduz tarefas operacionais e acelera o desenvolvimento de aplicações.
- SaaS entrega uma solução pronta, com foco do cliente em acesso, configuração e dados.
- Migrar responsabilidades ao provedor não elimina a responsabilidade do cliente por identidades, dados e configurações.
- A escolha correta depende do contexto; arquiteturas reais frequentemente combinam diferentes modelos.

