# Roteiro de Identificação de Informações Relevantes
## Projeto: Concepção de Solução para Gestão de Contratos do IFPE

**Equipe:** Vinícius Lima (Gerente do Projeto), Júlia Xavier, Charlys Farias, Flavio Miranda, Maria Passos, Vitor Malta  
**Cliente:** Marco Antônio Eugênio Araujo - IFPE  
**Período de Levantamento:** Setembro a Novembro de 2025  
**Versão:** 1.0  
**Data:** 02/12/2025

---

## 1. OBJETIVO DO ROTEIRO

Este documento descreve de forma estruturada como a equipe coletou, analisou e organizou as informações sobre o processo de Gestão de Contratos do IFPE. O roteiro comprova a metodologia aplicada e a rastreabilidade das informações obtidas, servindo como evidência do processo de levantamento de requisitos e análise de processos de negócio.

---

## 2. METODOLOGIA DE COLETA DE INFORMAÇÕES

### 2.1. Abordagem Geral
A equipe adotou uma abordagem **qualitativa e iterativa**, combinando:
- **Entrevistas semiestruturadas** com o cliente
- **Reuniões de validação** progressivas (modelo incremental)
- **Análise documental** de normas e legislação aplicável
- **Mapeamento visual** dos processos (BPMN)
- **Ferramentas colaborativas** para registro e organização das informações

### 2.2. Orientação Metodológica
O processo de levantamento seguiu as diretrizes das disciplinas integradas:
- **Gestão de Processos de Negócio (GPN):** Mapeamento AS-IS, identificação de gargalos, análise de causas
- **Planejamento e Gestão de Projetos (PGP):** Estruturação do TAP, definição de escopo, gestão de stakeholders
- **Sistemas de Gestão Empresarial (SGE):** Compreensão do contexto organizacional, requisitos funcionais

---

## 3. FONTES DE INFORMAÇÃO

### 3.1. Fonte Primária - Cliente
**Nome:** Marco Antônio Eugênio Araujo (Marcos Eugenio)  
**Vínculo:** IFPE - Conhecimento profundo do processo (ex-fiscal, atuação na gestão de contratos)  
**Papel:** Champion do projeto, responsável por validar todas as entregas e fornecer informações sobre o processo atual

**Justificativa da escolha:**
- Experiência prática como fiscal de contratos
- Conhecimento dos fluxos da Reitoria e dos Campi
- Acesso direto aos stakeholders-chave (Diretora de Licitação, Coordenadores, Gestores)
- Autoridade para validar formalmente os artefatos produzidos

### 3.2. Fontes Secundárias
- **Validação com stakeholders operacionais:** Durante as reuniões, Marco trouxe contribuições de fiscais e gestores de contrato que atuam nos campi
- **Documentação legal:** Lei nº 14.133/2021 (Lei de Licitações e Contratos), Decreto nº 11.246/2022 (Gestão e Fiscalização de Contratos)
- **Materiais institucionais:** Estrutura organizacional do IFPE, organograma, documentos contratuais vigentes

### 3.3. Ferramentas de Registro e Organização
- **Notion (Kanban):** Gestão de tarefas, acompanhamento de progresso, registro de decisões
- **GitHub:** Versionamento de documentos, artefatos de design, código do protótipo
- **Google Meet:** Reuniões remotas com gravação (quando autorizado)
- **WhatsApp:** Comunicação rápida com a equipe e cliente
- **E-mail institucional:** Comunicações formais e envio de artefatos para validação

---

## 4. CRONOLOGIA DO LEVANTAMENTO

### 4.1. Primeira Reunião - Setembro/2025 (18/09)
**Objetivo:** Compreensão inicial do problema e contexto organizacional

**Tópicos Discutidos:**
- Estrutura do IFPE: 16 campi + Reitoria (Matriz)
- Descentralização dos contratos de serviços continuados
- Principais dores identificadas:
  - Falta de padrão no gerenciamento contratual
  - Comunicação deficiente entre Reitoria e campi
  - Frustração na eficiência processual (renovações)
  - Risco de não conformidade em auditorias (TCU/CGU)
  - Dificuldade de antecipação de vencimentos contratuais
- Expectativas do cliente: solução open-source, centralização, dashboards operacionais
- Stakeholders envolvidos: Diretora de Licitação, Coordenadores de Contrato, Gestores, Fiscais (Requisitante, Técnico, Administrativo), Preposto (empresa), Setor Financeiro

**Informações-Chave Coletadas:**
- O orçamento é repassado pelo Governo Federal à Reitoria, mas a execução é descentralizada nos campi
- TCU e CGU cobram informações consolidadas da Reitoria, mas os dados estão fragmentados
- Cada campus tem fluxos e práticas próprias, sem padronização
- A gestão de vencimentos é reativa, dependendo da memória dos gestores
- Processo de renovação é manual, sem alertas automáticos

**Artefatos Produzidos após a Reunião:**
- Anotações da reunião (relato narrativo detalhado)
- Identificação preliminar de dores e oportunidades
- Esboço inicial do processo AS-IS

---

### 4.2. Segunda Reunião - Outubro/2025 (13/10)
**Objetivo:** Confirmação de stakeholders e detalhamento do fluxo AS-IS

**Tópicos Discutidos:**
- Confirmação dos stakeholders mapeados na primeira reunião
- Estrutura de governança detalhada:
  - **Reitoria/Matriz:** Diretora de Licitação (coordena licitação e reuniões com coordenadores)
  - **Campi:** Coordenador de Contrato (intermedia Reitoria e Direção local), Gestor de Contrato (execução direta), Fiscais (3 tipos), Preposto (empresa)
- Fluxo completo do processo AS-IS:
  - **Etapa 0:** Recebimento de recursos (Governo Federal → Reitoria → Campi)
  - **Etapa 1:** Planejamento da contratação (Campi elaboram TR → Reitoria valida e consolida)
  - **Etapa 2:** Licitação (Reitoria conduz → 17 contratos firmados: 16 campi + 1 Reitoria)
  - **Etapa 3:** Gestão do Contrato (execução mensal/trimestral com fiscalização)
  - **Etapa 4:** Renovação/Encerramento (análise de desempenho e continuidade)
- Características contratuais:
  - Validade de 10 anos
  - Pode iniciar até 2 anos após assinatura
  - Correção monetária (IPCA/inflação) aplicada em caso de atraso
- Rotina mensal de fiscalização:
  1. Fiscal Requisitante verifica se o serviço foi prestado
  2. Fiscal Técnico confirma conformidade técnica
  3. Fiscal Administrativo checa regularidade da empresa
  4. Preposto envia documentação fiscal
  5. Setor Financeiro processa pagamento

**Informações-Chave Coletadas:**
- O processo é altamente descentralizado: cada campi atua com autonomia após a licitação
- Não há padrão único de gestão: cada Gestor organiza seu time de forma diferente
- As etapas de verificação mensal são críticas para cumprimento e pagamento
- Comunicação Matriz-Campi ocorre principalmente nas fases iniciais e nas renovações
- Falta formalização do processo de renovação (manual, sem alertas, sem padronização)

**Artefatos Produzidos após a Reunião:**
- Diagrama de Escopo do Processo (preenchido e validado)
- Fluxograma AS-IS detalhado em BPMN
- Mapeamento completo de stakeholders e responsabilidades

---

### 4.3. Terceira Reunião - Novembro/2025 (Final de Novembro)
**Objetivo:** Validação final do AS-IS e detalhamento da etapa de Renovação/Repactuação

**Tópicos Discutidos:**
- Apresentação do fluxo AS-IS completo para validação formal
- Feedback do cliente sobre o mapeamento realizado
- **Adição crítica ao processo:** Etapa de Renovação/Repactuação (não formalizada anteriormente)
- Duas trilhas de renovação:
  - **Trilha A (Renovação Simples):** Empresa aceita índices oficiais (IPCA, inflação) → Aprovação Diretoria/Reitoria → Renovação rápida
  - **Trilha B (Renovação Complexa - Repactuação):** Empresa pede valores extras → Passa por CGU (validação legal) → Financeiro (verba) → Direção do Campi (decisão) → Aprovação ou Cancelamento
- Criticidade da antecipação: Gestor deve iniciar processo 6 meses antes do vencimento
- Consequências do atraso: Cancelamento do contrato → Interrupção do serviço → Nova licitação obrigatória

**Validações Realizadas:**
- Cliente validou formalmente o fluxo AS-IS mapeado em BPMN
- Cliente confirmou os 3 problemas priorizados:
  1. Falta de visibilidade centralizada dos contratos pela Reitoria
  2. Ausência de alertas automáticos para renovação/repactuação
  3. Falta de padronização na organização das informações contratuais
- Cliente aprovou o Termo de Abertura do Projeto (TAP) via e-mail formal

**Correções/Ajustes no Fluxo:**
- Inclusão formal da etapa de Renovação/Repactuação no fluxo AS-IS
- Detalhamento das duas trilhas (Simples vs. Complexa)
- Mapeamento dos atores envolvidos na repactuação (CGU, Financeiro, Direção)
- Definição dos prazos críticos (6 meses antes = alerta inicial, 3 meses = criticidade máxima)

**Artefatos Produzidos após a Reunião:**
- Fluxo AS-IS final validado (com etapa de Renovação/Repactuação)
- Documento "Pontos Primordiais para Resolver no Processo" (3 problemas detalhados)
- Análise de Dores consolidada
- Status Report 1 (consolidação da fase de Análise e Mapeamento)

---

## 5. TÉCNICAS DE LEVANTAMENTO UTILIZADAS

### 5.1. Entrevista Semiestruturada
**Descrição:** Reuniões com roteiro flexível, permitindo aprofundamento em tópicos emergentes

**Aplicação:**
- Primeira reunião: Perguntas abertas sobre o contexto, problemas e expectativas
- Segunda reunião: Perguntas direcionadas sobre stakeholders e fluxo operacional
- Terceira reunião: Validação do mapeamento e detalhamento de pontos críticos

**Vantagens:**
- Liberdade para explorar nuances do processo
- Captura de informações não previstas inicialmente (ex: etapa de repactuação)
- Construção de rapport com o cliente

### 5.2. Mapeamento de Processos (BPMN)
**Descrição:** Representação visual do fluxo atual usando notação BPMN 2.0

**Aplicação:**
- Transformação das informações coletadas em diagrama de processo
- Identificação de raias (swimlanes) por ator/organização
- Marcação de pontos problemáticos com esferas vermelhas no Diagrama de Escopo

**Vantagens:**
- Linguagem visual universal, facilitando validação com o cliente
- Identificação clara de gargalos e pontos de decisão
- Base para o futuro fluxo TO-BE

### 5.3. Análise Documental
**Descrição:** Estudo de legislação e normativos que regulam o processo

**Aplicação:**
- Lei nº 14.133/2021: Licitações e Contratos Administrativos
- Decreto nº 11.246/2022: Gestão e Fiscalização de Contratos na Administração Pública Federal
- Identificação de obrigações legais que impactam o processo (ex: validação pela CGU em repactuações)

**Vantagens:**
- Compreensão do contexto regulatório
- Identificação de restrições legais para a solução proposta
- Alinhamento com requisitos de conformidade (TCU/CGU)

### 5.4. Validação Progressiva (Modelo Incremental)
**Descrição:** Apresentação de artefatos parciais ao cliente para ajustes antes da finalização

**Aplicação:**
- Primeira reunião → Esboço inicial → Segunda reunião → Fluxo detalhado → Terceira reunião → Validação final
- Aprovação formal via email após cada marco principal

**Vantagens:**
- Redução de retrabalho
- Alinhamento contínuo com as expectativas do cliente
- Construção colaborativa do entendimento

### 5.5. Matriz CSD (Certezas, Suposições, Dúvidas)
**Descrição:** Ferramenta para organizar o conhecimento sobre o problema

**Aplicação:**
- **Certezas:** Descentralização, falta de padronização, risco de não conformidade
- **Suposições:** Solução open-source será viável, treinamento garantirá adesão
- **Dúvidas:** Quais fluxos de cada campus servem de modelo? Como será a integração tecnológica? Como garantir adesão dos stakeholders?

**Vantagens:**
- Estruturação clara do conhecimento adquirido
- Identificação de lacunas de informação
- Priorização de perguntas para as próximas reuniões

---

## 6. ORGANIZAÇÃO DAS INFORMAÇÕES COLETADAS

### 6.1. Estrutura de Armazenamento

**Notion (Workspace da Equipe):**
- Board Kanban com status das tarefas (Planejado, Em Progresso, Done)
- Registro de decisões tomadas em reuniões
- Base de conhecimento com anotações consolidadas
- Timeline do projeto com marcos principais

**GitHub (Repositório do Projeto):**
```
contract_management_ifpe/
│
├── docs/
│   ├── TAP.pdf
│   ├── Declaracao_de_Escopo.pdf
│   ├── Status_Report_1.pdf
│   ├── Relatorio_Licoes_Aprendidas.pdf
│   └── atas_reunioes/
│       ├── reuniao_1_setembro.md
│       ├── reuniao_2_outubro.md
│       └── reuniao_3_novembro.md
│
├── processes/
│   ├── diagrama_escopo.pdf
│   ├── fluxo_AS-IS_BPMN.bpmn
│   ├── fluxo_AS-IS_validado.pdf
│   └── pontos_criticos.pdf
│
├── design/
│   └── (wireframes e protótipos - próximas fases)
│
└── README.md
```

**Comunicação Formal:**
- E-mails com o cliente para envio de artefatos e solicitação de validação
- Aprovações formais registradas via resposta de e-mail

**Comunicação Informal:**
- WhatsApp para alinhamentos rápidos entre equipe e cliente
- Google Meet para reuniões síncronas

---

### 6.2. Rastreabilidade das Informações

Cada informação coletada foi rastreada desde sua origem até os artefatos finais:

| Informação | Fonte | Reunião | Artefato Final |
|------------|-------|---------|----------------|
| Estrutura organizacional (16 campi + Reitoria) | Marcos Eugenio | Reunião 1 (Set) | TAP, Diagrama de Escopo |
| Descentralização como gargalo principal | Marcos Eugenio | Reunião 1 (Set) | Status Report 1, Análise de Dores |
| Stakeholders e papéis (Gestor, Fiscais, Preposto) | Marcos Eugenio | Reunião 2 (Out) | Fluxo BPMN AS-IS, Diagrama de Escopo |
| Etapas do processo (0 a 4) | Marcos Eugenio | Reunião 2 (Out) | Fluxo BPMN AS-IS |
| Processo de Renovação/Repactuação | Marcos Eugenio + validação com fiscal/gestor | Reunião 3 (Nov) | Fluxo AS-IS Final, Pontos Críticos |
| Trilhas de renovação (Simples vs. Complexa) | Marcos Eugenio | Reunião 3 (Nov) | Fluxo AS-IS Final |
| Prazos críticos (6 meses = alerta, 3 meses = crítico) | Marcos Eugenio | Reunião 3 (Nov) | Pontos Críticos, Requisitos Funcionais |
| Legislação aplicável (Lei 14.133/2021, Decreto 11.246/2022) | Análise documental | Fase de Análise | Diagrama de Escopo, TAP |
| Órgãos fiscalizadores (TCU, CGU) | Marcos Eugenio | Reunião 1 (Set) | TAP, Diagrama de Escopo |

---

## 7. VALIDAÇÃO E APROVAÇÃO

### 7.1. Processo de Validação
Todos os artefatos principais passaram por validação formal com o cliente:

1. **Termo de Abertura do Projeto (TAP)**
   - Data de envio: 02/10/2025
   - Aprovado por: Marco Antônio Eugênio Araujo
   - Meio: E-mail institucional ("Ciente e de acordo")

2. **Fluxo AS-IS em BPMN**
   - Data de validação: 04/11/2025
   - Validado em: Reunião 3 via Google Meet
   - Ajustes realizados: Inclusão da etapa de Renovação/Repactuação

3. **Diagrama de Escopo**
   - Data de validação: 04/11/2025
   - Validado em: Reunião 3 via Google Meet
   - Aprovado sem alterações

4. **Análise de Dores e Pontos Críticos**
   - Data de validação: 04/11/2025
   - Validado em: Reunião 3 via Google Meet
   - Cliente confirmou os 3 problemas priorizados

### 7.2. Critérios de Aceitação
Para cada artefato, foram aplicados os seguintes critérios:
- **Completude:** Todas as informações relevantes estão presentes?
- **Acurácia:** As informações refletem a realidade do processo?
- **Clareza:** O artefato é compreensível para stakeholders técnicos e não técnicos?
- **Alinhamento:** O artefato está alinhado com os objetivos do projeto (definidos no TAP)?

---

## 8. PRINCIPAIS ACHADOS

### 8.1. Problemas Priorizados (Top 3)

**1. Falta de Visibilidade Centralizada dos Contratos pela Reitoria**
- **Impacto:** Ineficiência na tomada de decisão, risco de não conformidade em auditorias
- **Causa Raiz:** Ausência de sistema integrado, processo manual de consolidação

**2. Ausência de Alertas Automáticos para Renovação/Repactuação**
- **Impacto:** Risco de cancelamento de contratos, interrupção de serviços, necessidade de nova licitação
- **Causa Raiz:** Processo de renovação não formalizado, dependência da memória individual dos gestores

**3. Falta de Padronização na Organização das Informações Contratuais**
- **Impacto:** Dificuldade de auditoria, erros na fiscalização, comunicação ineficiente
- **Causa Raiz:** Cada gestor organiza "do seu jeito", ausência de template padrão

### 8.2. Oportunidades de Melhoria Identificadas

| Oportunidade | Valor Agregado |
|--------------|----------------|
| **Solução Tecnológica Centralizada** | Criar 'fonte única da verdade' para contratos, padronizando processos e eliminando coleta manual |
| **Automação da Gestão de Prazos** | Implementar notificações automáticas (6 meses antes = alerta, 3 meses = crítico), substituindo gestão reativa por proativa |
| **Painéis Operacionais (Dashboards)** | Desenvolver dashboards customizados (Reitoria e Campi) para apoiar tomada de decisão em tempo real |
| **Padronização de Papéis e Fluxos** | Definir templates e checklists para Gestores e Fiscais, garantindo uniformidade entre campi |
| **Repositório Centralizado de Documentos** | Armazenar TR, ART, laudos e demais anexos em local único e acessível |

---

## 9. PRÓXIMOS PASSOS

Com base nas informações coletadas e validadas, as próximas fases do projeto incluem:

1. **Finalização do Plano de Projeto Preliminar** (Em andamento - 50%)
   - EAP (Estrutura Analítica do Projeto)
   - Cronograma detalhado
   - Planos de Gerenciamento (Riscos, Comunicação, Custos)

2. **Design Conceitual da Solução** (Próxima fase)
   - Definição de Jornadas de Usuário (User Journeys) para cada stakeholder
   - Criação de Wireframes e Fluxos de Telas
   - Desenvolvimento do Protótipo Conceitual Navegável

3. **Modelagem do Processo TO-BE**
   - Redesenho do fluxo com as melhorias propostas
   - Mapeamento das automações e integrações necessárias

4. **Levantamento de Requisitos Funcionais e Não Funcionais**
   - Tradução das oportunidades em requisitos de software
   - Definição de critérios de qualidade e restrições técnicas

---

## 10. CONCLUSÃO

O processo de levantamento de informações foi conduzido de forma sistemática e colaborativa, utilizando técnicas apropriadas de engenharia de requisitos e análise de processos de negócio. A participação ativa do cliente (Marcos Eugenio) como champion foi fundamental para a qualidade e precisão das informações coletadas.

A rastreabilidade das informações está garantida através da documentação estruturada, versionamento no GitHub e registro formal de validações. Os 3 problemas priorizados estão claramente identificados e fundamentados nas informações coletadas, servindo como base para as próximas fases do projeto.

---

**Elaborado por:** Equipe 2 (Vinícius Lima, Júlia Xavier, Charlys Farias, Flavio Miranda, Maria Passos, Vitor Malta)  
**Aprovado por:** Marco Antônio Eugênio Araujo (Cliente - IFPE)  
**Data:** 02/12/2025