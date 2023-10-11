import pytest

def rot13enctest(msg):
    str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?æøåÆØÅ'
    str2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm987654321_/*.-+=?!@'
    str12 = msg.maketrans(str1, str2)

    return msg.translate(str12)


def test_if_rot13enc_works():
    msg = "hello is this getting ååå 987564 encrypted!?.."
    assert rot13enctest(msg) == str("uryyb/vf/guvf/trggvat/===/123546/rapelcgrq*...")