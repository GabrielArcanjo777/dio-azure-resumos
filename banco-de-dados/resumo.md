# Configurando uma Instância de Banco de Dados na Azure

## Escolha do serviço

O Azure oferece bancos relacionais, NoSQL e mecanismos especializados. Para SQL Server, as opções mais comuns são:

- **Banco de Dados SQL do Azure:** banco relacional como serviço, com alta disponibilidade e manutenção da plataforma gerenciadas.
- **Instância Gerenciada de SQL do Azure:** maior compatibilidade no nível de instância e recursos próximos ao SQL Server tradicional.
- **SQL Server em Máquina Virtual do Azure:** controle do sistema operacional e da instância, com maior responsabilidade administrativa.

A escolha depende de compatibilidade, nível de controle, esforço operacional, escalabilidade e custo. Este resumo usa como referência a criação de um Banco de Dados SQL do Azure.

## Configuração inicial

No portal, a criação começa pela definição da assinatura, do grupo de recursos e do nome do banco. Também é selecionado ou criado um **servidor lógico**, que agrupa configurações administrativas e de conectividade para os bancos associados.

As decisões principais incluem:

- região de implantação;
- ambiente de carga de trabalho;
- camada de serviço e quantidade de recursos computacionais;
- armazenamento e redundância de backup;
- autenticação e conta administrativa;
- possibilidade de usar uma base de exemplo para testes.

O portal apresenta uma estimativa de custo antes da implantação. A capacidade deve ser dimensionada com base na carga real e revisada após a coleta de métricas.

## Rede e conectividade

O acesso pode ocorrer por endpoint público, regras de firewall, integração com rede virtual ou endpoint privado. Liberar todo o tráfego público não é uma boa prática. O ideal é permitir apenas origens necessárias ou manter a comunicação em rede privada.

Após a implantação, a aplicação usa o nome do servidor, o nome do banco, o método de autenticação e uma conexão criptografada. Segredos de conexão não devem ficar gravados no código; podem ser armazenados no Azure Key Vault ou substituídos por autenticação baseada em identidade quando compatível.

## Segurança e governança

Controles importantes incluem:

- autenticação pelo Microsoft Entra ID e princípio do menor privilégio;
- criptografia dos dados em repouso e em trânsito;
- auditoria, alertas e avaliação de vulnerabilidades;
- Microsoft Defender para SQL quando adequado ao risco;
- classificação e proteção de dados sensíveis;
- tags, políticas e bloqueios para governança do recurso.

## Operação, disponibilidade e custos

Serviços gerenciados automatizam tarefas de infraestrutura, atualizações da plataforma e backups, mas o cliente ainda deve validar retenção, restauração e recuperação. Métricas de CPU, dados e log, conexões, bloqueios e consultas ajudam a detectar gargalos.

Escala, alta disponibilidade, replicação geográfica e redundância devem seguir os objetivos de recuperação do negócio. Camadas e recursos superdimensionados aumentam custos; capacidade insuficiente prejudica desempenho. Alertas de orçamento e revisões periódicas ajudam a manter o equilíbrio.

## Insights/Aprendizados

- O tipo de banco deve ser escolhido pela necessidade da aplicação, e não apenas pela familiaridade com uma tecnologia.
- Um serviço gerenciado reduz tarefas de infraestrutura, mas não elimina cuidados com dados, acessos e recuperação.
- A configuração de rede deve seguir o menor nível de exposição possível.
- Credenciais não devem ser armazenadas no código ou em arquivos versionados.
- Backup só é confiável quando a estratégia de restauração também é conhecida e testada.

