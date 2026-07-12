# Construindo Arquiteturas no Azure

## Estrutura global e organização

Uma arquitetura no Azure começa pela escolha das localidades e pela organização dos recursos:

- **Regiões:** áreas geográficas que contêm um ou mais datacenters e disponibilizam conjuntos de serviços.
- **Zonas de disponibilidade:** grupos fisicamente separados de datacenters dentro de uma região, com energia, refrigeração e rede independentes.
- **Grupos de recursos:** contêineres lógicos para recursos que compartilham gerenciamento e ciclo de vida.
- **Assinaturas:** limites de cobrança, acesso, políticas e cotas.
- **Grupos de gerenciamento:** camada para aplicar governança a várias assinaturas.

Região e zona devem ser escolhidas conforme latência, disponibilidade dos serviços, custo, residência de dados e requisitos de continuidade.

## Blocos de uma solução

Arquiteturas de nuvem normalmente combinam:

- **Entrada e entrega:** DNS, proteção de borda, gateways e balanceamento de carga.
- **Rede:** redes virtuais, sub-redes, rotas, firewalls e conectividade híbrida.
- **Computação:** máquinas virtuais, contêineres, serviços de aplicativos e funções.
- **Dados:** armazenamento de objetos e arquivos, bancos relacionais, NoSQL e cache.
- **Identidade e segurança:** Microsoft Entra ID, funções de acesso, identidades gerenciadas e Key Vault.
- **Operação:** Azure Monitor, logs, métricas, alertas, automação e gerenciamento de custos.

Esses componentes devem ser selecionados a partir dos requisitos da carga, evitando complexidade sem benefício mensurável.

## Disponibilidade, escala e recuperação

Alta disponibilidade reduz interrupções dentro do ambiente operacional. O uso de múltiplas instâncias, zonas, balanceamento e serviços gerenciados elimina pontos únicos de falha. Escala vertical aumenta a capacidade de um recurso; escala horizontal adiciona instâncias e costuma oferecer mais elasticidade e resiliência.

Recuperação de desastre trata falhas maiores e pode exigir replicação para outra região. O desenho deve considerar:

- **RTO (Recovery Time Objective):** tempo máximo desejado para restaurar o serviço.
- **RPO (Recovery Point Objective):** perda máxima de dados aceitável medida em tempo.

Backups, replicação e planos de contingência precisam ser testados. Distribuir recursos sem compreender dependências não garante resiliência.

## Segurança e governança por design

Uma base segura aplica menor privilégio, autenticação forte, segmentação de rede, criptografia, gestão de segredos e monitoramento contínuo. Tags, Azure Policy, controle de acesso baseado em função e padrões de nomenclatura tornam o ambiente auditável e consistente.

Separar ambientes de desenvolvimento, homologação e produção reduz riscos. Infraestrutura como código ajuda a repetir implantações, revisar mudanças e diminuir configurações manuais divergentes.

## Custo, desempenho e evolução

As decisões arquiteturais sempre envolvem compensações. Mais redundância pode elevar custo; maior desempenho pode aumentar consumo; um serviço gerenciado pode reduzir operação, mas impor limites específicos. Métricas e requisitos reais devem orientar o dimensionamento.

Uma boa arquitetura evolui por ciclos: definir requisitos, projetar, implantar, observar, testar falhas e otimizar. Segurança, confiabilidade, desempenho, operação e custo devem ser avaliados em conjunto.

## Insights/Aprendizados

- Arquitetura começa pelos requisitos do negócio, não pela escolha isolada de serviços.
- Grupos de recursos, assinaturas e grupos de gerenciamento têm papéis diferentes na organização e governança.
- Alta disponibilidade, backup e recuperação de desastre resolvem problemas distintos e complementares.
- RTO e RPO transformam expectativas de continuidade em critérios de projeto.
- Segurança, observabilidade e controle de custos precisam nascer com a solução e evoluir com ela.
