# API de Sistema de Eventos

Você vai construir uma API onde usuários podem criar eventos, comprar/reservar ingressos e deixar avaliações.

### Entidades principais

- **User**
  - `id`
  - `name`
  - `email`

- **Event**
  - `id`
  - `title`
  - `description`
  - `location`
  - `date`
  - `capacity`
  - `status`

- **Ticket**
  - `id`
  - `eventId`
  - `userId`
  - `type`
  - `price`
  - `status`

- **Review**
  - `id`
  - `eventId`
  - `userId`
  - `rating`
  - `comment`

### Regras
- Um evento possui uma capacidade máxima.
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