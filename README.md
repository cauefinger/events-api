# API de Sistema de Eventos

Você vai construir uma API onde usuários podem criar eventos, comprar/reservar ingressos e deixar avaliações.

## Tarefas
[OK] Criar depends.py e fazer o gerenciamento de sessao com o DB postgreSQL (Caue)
[OK] Trocar os tipos dos models para UUID
[OK] Usar ForeignKey no ticket, review e event 
[ ] Criar um endpoint para venda de tickets (Visualizar tickets disponíveis, comprar ticket, não pode vender mais tickets que a capacidade do evento)
[ ] Não pode vender ingresso para um evento fechado
[ ] Criar um job que todo dia procure os eventos que acabaram e setar status para ENDED
[ ] Criar endpoint para avaliar evento (só pode avaliar um evento se aquele usuário tiver ticket para aquele evento)

### Entidades principais

- **User** OK
  - `id`
  - `name`
  - `email`

- **Event** OK
  - `id`
  - `title`
  - `description`
  - `location`
  - `date`
  - `capacity`
  - `status`

- **Ticket** OK 
  - `id`
  - `eventId`
  - `userId`
  - `type`
  - `price`
  - `status`

- **Review** OK
  - `id`
  - `eventId`
  - `userId`
  - `rating`
  - `comment`

### Regras
- Não pode vender mais ingressos que a capacidade.
- Um usuário não pode comprar dois ingressos do mesmo tipo para o mesmo evento.
- Não pode comprar ingresso para evento encerrado.
- Só pode avaliar um evento quem possui ingresso.
- Um usuário só pode fazer uma avaliação por evento.
- Não pode alterar um evento que já começou.
- Cancelar um ingresso libera uma vaga.
- GET /events deve retornar apenas eventos abertos por padrão.
- Eventos podem ter categorias: CONCERT, SPORT, CONFERENCE, etc.

### Running local

`uv run uvicorn events_api.main:app --reload`