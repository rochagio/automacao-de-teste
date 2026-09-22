Feature: Login
    Scenario: Login válido
        Given que o usuário acessa a página de login
        When ele realiza login com usuário válido
        Then ele deve ser redirecionado para a página de inventário

    Scenario: Login inválido
        Given que o usuário acessa a página de login
        When ele realiza login com usuário inválido
        Then ele deve visualizar mensagem de erro

    Scenario: Login bloqueado
        Given que o usuário acessa a página de login
        When ele realiza login com usuário "locked_out_user" e senha "secret_sauce"
        Then ele deve visualizar mensagem de usuário bloqueado