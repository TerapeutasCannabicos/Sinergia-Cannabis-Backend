# App Cannabis

- [Administrador](#Administrador)
- [Advogado](#advogado)
- [Paciente](#paciente)
- [Gestor](#gestor)
- [Medico](#medico)
- [Outros](#outros)
- [Responsavel](#responsavel)

---

## Medicos

### Campos

| Campo                   | Tipo                                 |
| ---------------         | ------------------------------------ |
| **nome**                | string(required)                     |
| **sobrenome**           | string(required)                     |
| **especialidade**       | string(required)                     |
| **sexo**                | string(required)                     |
| **bio**                 | string                               |
| **foto_perfil**         | string(required)                     |
| **email**               | string(required)                     |
| **facebook**            | string                               |
| **twitter**             | string                               |
| **instagram**           | string                               |
| **cpf**                 | string(required)                     |
| **rg**                  | string(required)                     |
| **celular**             | string(required)                     |
| **telefone_secundario** | string                               |   
| **endereco**            | string(required)                     |
| **bairro**              | string(required)                     |
| **numero**              | integer(required)                    |
| **complemento**         | string(required)                     |
| **cidade**              | string(required)                     |
| **estado**              | string(required)                     |
| **cep**                 | string(required)                     |
| **confirmacao_cadastro**| Boolean(auto)(confirmação cadastro)  |
| **password**            | LargeBinary(required)                |
| **paciente**            | relationship                         |
| **administrador**       | relationship                         |


### Endpoints

| Função                   | Método | Endpoint                                        |
| ------------------------ | ------ | ----------------------------------------------- |
| **get**                  | GET    | `/medico/{medico_id}`                           |
| **get current user**     | GET    | `/medico/current`                               |
| **create**               | POST   | `/medico`                                       |
| **update**               | PUT    | `/medico/{medico_id}`                           |
| **partial update**       | PATCH  | `/medico/{medico_id}`                           |
| **delete**               | DELETE | `/medico/{medico_id}`                           |
| **email validation**     | GET    | `medico-confirm`                                |
| **email reset password** | POST   | `pw-email`                                      |
| **password reset**       | PATCH  | `pw-reset`                                      |

---

## Administrador

### Campos

| Campo                   | Tipo                                 |
| ---------------         | ------------------------------------ |
| **nome**                | string(required)                     |
| **sobrenome**           | string(required)                     |
| **email**               | string(required)                     |
| **cpf**                 | string(required)                     |
| **celular**             | string(required)                     |
| **telefone_secundario** | string                               |   
| **endereco**            | string(required)                     |
| **bairro**              | string(required)                     |
| **numero**              | integer(required)                    |
| **complemento**         | string(required)                     |
| **cidade**              | string(required)                     |
| **estado**              | string(required)                     |
| **cep**                 | string(required)                     |
| **password**            | LargeBinary(required)                |
| **paciente**            | relationship                         |
| **gestor**              | relationship                         |
| **medico**              | relationship                         |
| **outros**              | relationship                         |
| **advogado**            | relationship                         |


### Endpoints

| Função                   | Método | Endpoint                                                           |
| ------------------------ | ------ | -------------------------------------------------------------------|
| **get**                  | GET    | `/administrador/{administrador_id}`                                |
| **get current user**     | GET    | `/administrador/lista`                                             |
| **create**               | POST   | `/administrador`                                                   |
| **update**               | PUT    | `/administrador/{administrador_id}`                                |
| **partial update**       | PATCH  | `/administrador/{administrador_id}`                                |
| **delete**               | DELETE | `/administrador/{administrador_id}`                                |
| **email validation**     | GET    | `administrador-confirm`                                            |
| **email reset password** | POST   | `pw-email`                                                         |
| **password reset**       | PATCH  | `pw-reset`                                                         |
| **register confirm**     | PATCH  | `register-confirm`                                                 |
| **register accept**      | PATCH  | `register-accept-advogado/{administrador_id}/{advogado_id}`        |
| **confirm cadastro**     | PATCH  | `register-accept-gestor/{administrador_id}/{gestor_id}`            |
| **confirm cadastro**     | PATCH  | `register-accept-medico/{administrador_id}/{medico_id}`            |
| **confirm cadastro**     | PATCH  | `register-accept-outros/{administrador_id}/{outros_id}`            |
| **confirm cadastro**     | PATCH  | `register-accept-paciente/{administrador_id}/{paciente_id}`        |
| **confirm cadastro**     | PATCH  | `register-accept-responsavel/{administrador_id}/{responsavel_id}`  |
| **show medicos**         | GET    | `/show/medico`                                                     |
| **show pacientes**       | GET    | `/show/medico/paciente/{medico_id}`                                |


---

## Advogado

### Campos

| Campo                   | Tipo                                 |
| ---------------         | ------------------------------------ |
| **nome**                | string(required)                     |
| **sobrenome**           | string(required)                     |
| **email**               | string(required)                     |
| **cpf**                 | string(required)                     |
| **celular**             | string(required)                     |
| **telefone_secundario** | string                               |   
| **endereco**            | string(required)                     |
| **bairro**              | string(required)                     |
| **numero**              | integer(required)                    |
| **complemento**         | string(required)                     |
| **cidade**              | string(required)                     |
| **estado**              | string(required)                     |
| **cep**                 | string(required)                     |
| **confirmacao_cadastro**| Boolean(auto)(confirmação cadastro)  |
| **password**            | LargeBinary(required)                |
| **paciente**            | relationship                         |
| **administrador**       | relationship                         |


### Endpoints

| Função                   | Método | Endpoint                                        |
| ------------------------ | ------ | ----------------------------------------------- |
| **get**                  | GET    | `/advogado/{advogado_id}`                       |
| **get current user**     | GET    | `/advogado/lista`                               |
| **create**               | POST   | `/advogado`                                     |
| **update**               | PUT    | `/advogado/{advogado_id}`                       |
| **partial update**       | PATCH  | `/advogado/{advogado_id}`                       |
| **delete**               | DELETE | `/advogado/{advogado_id}`                       |
| **email validation**     | GET    | `advogado-confirm`                              |
| **email reset password** | POST   | `pw-email`                                      |
| **password reset**       | PATCH  | `pw-reset`                                      |

---

## Gestor

### Campos

| Campo                   | Tipo                                 |
| ---------------         | ------------------------------------ |
| **nome**                | string(required)                     |
| **sobrenome**           | string(required)                     |
| **email**               | string(required)                     |
| **cpf**                 | string(required)                     |
| **celular**             | string(required)                     |
| **telefone_secundario** | string                               |   
| **endereco**            | string(required)                     |
| **bairro**              | string(required)                     |
| **numero**              | integer(required)                    |
| **complemento**         | string(required)                     |
| **cidade**              | string(required)                     |
| **estado**              | string(required)                     |
| **cep**                 | string(required)                     |
| **confirmacao_cadastro**| Boolean(auto)(confirmação cadastro)  |
| **password**            | LargeBinary(required)                |
| **paciente**            | relationship                         |
| **administrador**       | relationship                         |


### Endpoints

| Função                   | Método | Endpoint                                        |
| ------------------------ | ------ | ----------------------------------------------- |
| **get**                  | GET    | `/gestor/{gestor_id}`                           |
| **get current user**     | GET    | `/gestor/lista`                                 |
| **create**               | POST   | `/gestor`                                       |
| **update**               | PUT    | `/gestor/{gestor_id}`                           |
| **partial update**       | PATCH  | `/gestor/{gestor_id}`                           |
| **delete**               | DELETE | `/gestor/{gestor_id}`                           |
| **email validation**     | GET    | `gestor-confirm`                                |
| **email reset password** | POST   | `pw-email`                                      |
| **password reset**       | PATCH  | `pw-reset`                                      |

---

## Outros

### Campos

| Campo                   | Tipo                                 |
| ---------------         | ------------------------------------ |
| **nome**                | string(required)                     |
| **sobrenome**           | string(required)                     |
| **email**               | string(required)                     |
| **cpf**                 | string(required)                     |
| **celular**             | string(required)                     |
| **telefone_secundario** | string                               |   
| **endereco**            | string(required)                     |
| **bairro**              | string(required)                     |
| **numero**              | integer(required)                    |
| **complemento**         | string(required)                     |
| **cidade**              | string(required)                     |
| **estado**              | string(required)                     |
| **cep**                 | string(required)                     |
| **confirmacao_cadastro**| Boolean(auto)(confirmação cadastro)  |
| **permissao adm**       | Boolean(auto)(permissao)             |
| **nivel_permissao**     | integer                              |
| **password**            | LargeBinary(required)                |
| **paciente**            | relationship                         |
| **administrador**       | relationship                         |
| **permissao**           | relationship                         |


### Endpoints

| Função                   | Método | Endpoint                                        |
| ------------------------ | ------ | ----------------------------------------------- |
| **get**                  | GET    | `/outros/{outros_id}`                           |
| **permissao outros**     | GET    | `/permission/outros`                            |
| **permissao adm**        | PATCH  | `/permissao/adm/outros/{outros_id}`             |
| **get current user**     | GET    | `/outros/lista`                                 |
| **create**               | POST   | `/outros`                                       |
| **update**               | PUT    | `/outros/{outros_id}`                           |
| **partial update**       | PATCH  | `/outros/{outros_id}`                           |
| **delete**               | DELETE | `/outros/{outros_id}`                           |
| **email validation**     | GET    | `outros-confirm`                                |
| **email reset password** | POST   | `pw-email`                                      |
| **password reset**       | PATCH  | `pw-reset`                                      |

---

## Paciente

### Campos

| Campo                   | Tipo                                 |
| ---------------         | ------------------------------------ |
| **nome**                | string(required)                     |
| **sobrenome**           | string(required)                     |
| **data_nascimento**     | Date                                 |
| **cpf**                 | string(required)                     |
| **rg**                  | string(required)                     |
| **documentos_pessoais** | string(required)                     |
| **diagnostico**         | string(required)                     |
| **laudo_medico**        | string(required)                     |
| **receita_medica**      | string(required)                     |  
| **endereco**            | string(required)                     |
| **bairro**              | string(required)                     |
| **numero**              | integer(required)                    |
| **complemento**         | string(required)                     |
| **cidade**              | string(required)                     |
| **estado**              | string(required)                     |
| **confirmacao_cadastro**| Boolean(auto)(confirmação cadastro)  |
| **responsavel**         | relationship                         |
| **gestor**              | relationship                         |
| **medico**              | relationship                         |
| **outros**              | relationship                         |
| **administrador**       | relationship                         |
| **advogado**            | relationship                         |

### Endpoints

| Função                   | Método | Endpoint                                        |
| ------------------------ | ------ | ----------------------------------------------- |
| **get**                  | GET    | `/paciente/{paciente_id}`                       |
| **get current user**     | GET    | `/paciente/lista`                               |
| **create**               | POST   | `/paciente`                                     |
| **update**               | PUT    | `/paciente/{paciente_id}`                       |
| **partial update**       | PATCH  | `/paciente/{paciente_id}`                       |
| **delete**               | DELETE | `/paciente/{paciente_id}`                       |
| **email validation**     | GET    | `paciente-confirm`                              |
| **email reset password** | POST   | `pw-email`                                      |
| **password reset**       | PATCH  | `pw-reset`                                      |

---

## Responsavel

### Campos

| Campo                   | Tipo                                 |
| ---------------         | ------------------------------------ |
| **nome**                | string(required)                     |
| **sobrenome**           | string(required)                     |
| **email**               | string(required)                     |
| **cpf**                 | string(required)                     |
| **rg**                  | string(required)                     |
| **celular**             | string(required)                     |
| **telefone_secundario** | string                               |  
| **endereco**            | string(required)                     |
| **bairro**              | string(required)                     |
| **numero**              | integer(required)                    |
| **complemento**         | string(required)                     |
| **cidade**              | string(required)                     |
| **estado**              | string(required)                     |
| **cep**                 | string(required)                     |
| **confirmacao_cadastro**| Boolean(auto)(confirmação cadastro)  |
| **password**            | LargeBinary(required)                |
| **paciente**            | relationship                         |

### Endpoints

| Função                   | Método | Endpoint                                        |
| ------------------------ | ------ | ----------------------------------------------- |
| **get**                  | GET    | `/responsavel/{responsavel_id}`                 |
| **get current user**     | GET    | `/responsavel/lista`                            |
| **create**               | POST   | `/responsavel`                                  |
| **update**               | PUT    | `/responsavel/{responsavel_id}`                 |
| **partial update**       | PATCH  | `/responsavel/{responsavel_id}`                 |
| **delete**               | DELETE | `/responsavel/{responsavel_id}`                 |
| **email validation**     | GET    | `responsavel-confirm`                           |
| **email reset password** | POST   | `pw-email`                                      |
| **password reset**       | PATCH  | `pw-reset`                                      |

---
## Login

### Campos

| Campo        | Tipo             |
| ------------ | ---------------- |
| **email**    | string(required) |
| **password** | string(required) |

### Endpoints

| Método | Endpoint         | Função                                                                                                                     |
| ------ | ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| POST   | `/login`         | **Login padrão com email e senha, retorna um fresh token para acesso, um token para refresh e o usuário que está logando**                             |

### Exemplos

```c
POST /token

{
    "email": "user@email.com",
    "password": "123456"
}
```

```c
{
    "token": "eyJpYXQiOjE1OTc1OTYwMDIsIm5iZiI6MTU5NzU5NjAw",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
    "user": ...
}
```


## Storage

### Endpoints

| Método | Endpoint                        | Função                                                                                                                                                                                                                                                                                                                                                                              |
| ------ | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET    | `/files/<file_format>` | Sempre que for fazer o update de uma imagem, deve ser feito através de um **PUT** para a url retornada por esse endpoint. **O nome da file deve ser o retornado por esse endpoint.** Após o update realizado com sucesso o nome da file **deve ser salvo no database** através de um **PUT** ou **PATCH** na entidade adequada, ou **no caso de photo quando estiver sendo criada** |

### Exemplos

Para salvar uma foto para o `procedure` com `id: 2`, primeiro pegamos a pre-signed url para o upload:

```c
GET /medias/put_url?media_format=jpg

}
    "media_url": "https://nyc3.digitaloceanspaces.com/storage-fluxo/harmonic/
    64af2ae1313e4c4294a5eb763b8b7f4b.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&
    X-Amz-Credential=UBRNRUAD5ZIAECGZ6M63%2F20200816%2Fnyc3%2Fs3%2Faws4_request&
    X-Amz-Date=20200816T170646Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&
    X-Amz-Signature=11ec9c9ad10ae890620d232af2c7125459929a019ccb8effb0f1652ac05ab149",
    "media_name": "64af2ae1313e4c4294a5eb763b8b7f4b.jpg"
}
```

Fazemos **primeiro** um **PUT** para a `media_url` retornada e enviamos a imagem com o nome retornado em `media_name`. **Somente após o sucesso no PUT criamos a media**:

```c
POST /procedures/2/medias

{
	"before_procedure":true,
	"date":"03-12-2020",
	"angle":"any",
	"media_name":"64af2ae1313e4c4294a5eb763b8b7f4b.jpg",
	"media_type":"photo"
}
```
Caso o campo de **media seja atualizado** para qualquer entidade **a media anterior é automaticamente deletada**.


---

## Pasta Pacientes

### Campos

| Campo                   | Tipo                                 |
| ---------------         | ------------------------------------ |
| **nome**                | string                               |


### Endpoints

| Função                   | Método | Endpoint                                        |
| ------------------------ | ------ | ----------------------------------------------- |
| **get**                  | GET    | `/responsavel/{responsavel_id}`                 |
| **get current user**     | GET    | `/responsavel/lista`                            |
| **create**               | POST   | `/responsavel`                                  |
| **update**               | PUT    | `/responsavel/{responsavel_id}`                 |
| **partial update**       | PATCH  | `/responsavel/{responsavel_id}`                 |
| **delete**               | DELETE | `/responsavel/{responsavel_id}`                 |
| **email validation**     | GET    | `responsavel-confirm`                           |
| **email reset password** | POST   | `pw-email`                                      |
| **password reset**       | PATCH  | `pw-reset`                                      |

---