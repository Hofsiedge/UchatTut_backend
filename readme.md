# URLs & conventions
## General
* JSON Web Token is replaced with user\_id for now (so the `Authorization` header should be set to user id)

## HTTP
* auth/ ...
* api/ ...

### REST API
* api/usr:
    * GET       api/usr/<id>    - get a user by id
* api/q:
    * GET       api/q/          - search across API (constrained by JSON fields like `resource-type`)
* api/msg:
    * GET       api/msg/<id>    - get a message by id
    * POST      api/msg/        - create a message (`chat_id` required), get `msg_id`
    * DELETE    api/msg/<id>    - delete a message by id
    * PUT       api/msg/<id>    - replace a message by id (new message required)
* api/chat:
    * GET       api/chat/       - get the list of available chats
    * GET       api/chat/<id>   - get last ... messages from the chat
    * POST      api/chat/       - create a chat, get `chat_id`
    * DELETE    api/chat/<id>   - delete a chat
* api/img:
    * POST      api/img/        - upload an image, get id
    * GET       api/img/<id>    - get an image by id
    * DELETE    api/img/<id>    - delete an image by id

## Web-socket
* WS connection is only used to send notifications to the client
* WS request on /ws initiates a WS connection


# Architecture draft
* Event
    * ChatEvent
        * MessageAction
        * ChatAction
    * TaskEvent
    * ScheduleEvent
* Resource
    * User
    * Chat
    * Message
    * Image
    * Voice?
    * Document


```
User {
    "id":       user_id,
    "name":     "name",
    "surname":  "surname",
    "phone":    "phone number",
    "address":  "address",
    "photo:     "api/img/..."
    ...
}

Chat {
    "id":       chat_id,
    "users":    [user_id, user_id, ...]
    "name":     "chat name"
}

Attachment {
    "attachment_type": "image",                         <-- image | message | document | voice?
    "url": "/api/img/12"
}

Message {
    "id":           message_id,
    "sender":       sender_id,
    "timestamp":    timestamp,
    "text":         "message text",
    "attachments":  [
        {... Attachment ...},
        {... Attachment ...},
    ],
}

Image {
    "id":       image_id,
    ["idx":     {... semantic_index ...},]
    ["caption": "text",                  ]
    "b64":      base64_image
}

...

Event {
    "type": "event type",
    "event": {... Event ...}
}

MessageAction {
    "action":   "send",                                 <-- send | read | delete | edit
    "id":       message_id
}

ChatAction {
    "action":   "delete",                               <-- delete | invite | archive? | create? | ...
    "id":       chat_id
}
```
