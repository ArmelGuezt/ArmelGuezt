# GitHub Profile V2.0 - Guia de publicação

## Antes de publicar

- Revise a prévia HTML e o README. Nenhum repositório foi criado ou alterado durante a preparação.
- Confirme o usuário ArmelGuezt e a divulgação pública das informações selecionadas.
- Crie ou reutilize o repositório especial público ArmelGuezt/ArmelGuezt. Se já houver README, preserve uma cópia e revise as alterações antes de substituir.
- Envie o conteúdo desta pasta para a branch padrão (normalmente main), mantendo as pastas assets, scripts e .github/workflows. O README.md deve ficar na raiz.
- Em Settings > Actions, permita a execução de workflows. A rotina solicita contents: write apenas para atualizar os SVGs e o JSON. A política da conta pode impedir o push automático.
- Execute Actions > Refresh public profile statistics > Run workflow. Verifique os logs e as métricas exibidas. A atualização seguinte está configurada para 06:17 UTC diariamente; a execução pode atrasar.

## Métricas e limitações

- A captura de 26/11/2026 veio das buscas do conector GitHub: três repositórios públicos encontrados, com 6, 2 e 2 commits retornados na busca. Não são totais históricos, nem necessariamente commits de autoria do titular.
- O script de atualização consulta repositórios públicos e até 10 commits recentes por repositório. As estrelas são somadas após a primeira execução bem-sucedida.
- O calendário de contribuições ainda não foi verificado; sua geração depende da API GraphQL e das permissões do token fornecido automaticamente pelo GitHub Actions. Não é necessário criar um token pessoal. Se a consulta falhar, o cartão informa indisponibilidade e oferece o perfil como alternativa.
- Não há serviços terceiros de estatísticas, contadores de visitantes ou scripts remotos no README. A animação SVG é decorativa; a exibição depende do cliente GitHub e das preferências de movimento. A prévia HTML é local e não representa exatamente o layout nativo do GitHub.
- A rotina remota ainda não foi executada; nenhum agendamento foi ativado. O script e os SVGs locais foram preparados e validados.
- Nenhuma credencial deve ser enviada ao repositório.

## Teste local

```bash
python3 scripts/render.py
```

Para buscar dados atuais da API pública, com conexão de rede:

```bash
python3 scripts/refresh.py
```

Sem token, a consulta opcional do calendário é ignorada. O README usa caminhos relativos para os SVGs.
