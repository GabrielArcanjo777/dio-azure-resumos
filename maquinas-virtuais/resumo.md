# Criando Máquinas Virtuais na Azure

## Conceito de máquina virtual

Uma máquina virtual (VM) fornece processamento, memória, armazenamento e rede virtualizados. No Azure, ela representa um modelo de **Infraestrutura como Serviço (IaaS)**: a Microsoft mantém a infraestrutura física e a camada de virtualização, enquanto o cliente administra o sistema operacional, as atualizações, as aplicações e grande parte da configuração de segurança.

VMs são indicadas quando a solução exige controle do sistema operacional, compatibilidade com aplicações legadas ou configurações que uma plataforma totalmente gerenciada não oferece.

## Planejamento da implantação

Antes de criar a VM, é necessário definir:

- **Assinatura e grupo de recursos:** determinam cobrança, organização e ciclo de vida.
- **Região e disponibilidade:** afetam latência, preço, conformidade e resiliência.
- **Imagem:** sistema operacional e, em alguns casos, software pré-instalado.
- **Tamanho:** combinação de vCPUs, memória, capacidade de disco e desempenho de rede.
- **Autenticação:** chaves SSH são recomendadas para Linux; senhas devem seguir políticas fortes.
- **Rede:** rede virtual, sub-rede, endereço IP e regras de entrada e saída.
- **Discos:** disco do sistema operacional e discos de dados, com desempenho adequado à carga.

## Etapas de criação no portal

O assistente de criação organiza a configuração em abas:

1. **Básico:** projeto, região, disponibilidade, imagem, tamanho e credenciais.
2. **Discos:** tipo de disco do sistema e discos adicionais.
3. **Rede:** rede virtual, sub-rede, IP público e grupo de segurança de rede.
4. **Gerenciamento e monitoramento:** identidade, desligamento automático, diagnóstico e alertas.
5. **Avançado e tags:** extensões, dados de inicialização e metadados de organização.
6. **Revisar + criar:** validação final das configurações e do custo estimado.

## Acesso e segurança

Um **Network Security Group (NSG)** controla o tráfego permitido. Portas administrativas, como SSH (22) e RDP (3389), não devem ficar abertas indiscriminadamente para a internet; o acesso pode ser limitado por endereço de origem, VPN, Azure Bastion ou mecanismos de acesso temporário.

Também são importantes a aplicação de atualizações, o princípio do menor privilégio, a proteção dos discos, o uso de identidades gerenciadas quando possível e a habilitação de logs, métricas, alertas e backup.

## Disponibilidade, operação e custos

Zonas de disponibilidade e conjuntos de disponibilidade reduzem riscos de falha quando há mais de uma VM. Balanceamento de carga e conjuntos de dimensionamento ajudam a distribuir requisições e ajustar capacidade.

O custo depende principalmente do tamanho, tempo de execução, discos, licenças e tráfego de saída. Desligar o sistema operacional não necessariamente interrompe a cobrança de computação; para liberar os recursos computacionais, a VM precisa ficar no estado **Parada (desalocada)**. Discos e outros recursos associados podem continuar gerando custo mesmo assim.

## Insights/Aprendizados

- Uma VM oferece flexibilidade, mas também amplia a responsabilidade operacional do cliente.
- Região, tamanho e imagem devem refletir requisitos técnicos, financeiros e de conformidade.
- Expor portas de administração publicamente aumenta o risco e deve ser evitado sempre que possível.
- Monitoramento, backup e estratégia de disponibilidade precisam fazer parte do desenho inicial.
- Recursos ociosos devem ser desalocados ou removidos com cuidado para controlar gastos.

