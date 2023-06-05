from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    #  Verificar quando o tipo de key é inválido
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "key")

    #  Verificar quando o tipo de message é inválido
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 2)

    #  Verificar quando key não é um índice válido
    assert encrypt_message("test", 100) == "tset"

    #  Verificar a lógica de criptografia quando key é ímpar
    assert encrypt_message("test", 1) == "t_tse"

    #  Verificar a lógica de criptografia quando key é par
    assert encrypt_message("test", 2) == "ts_et"

    # Verificar quando key é igual ao tamanho da mensagem
    assert encrypt_message("test", 3) == "set_t"
