from typing import Optional

from pydantic import BaseModel, field_validator


class Cliente(BaseModel):
    nome: str
    data_nascimento: str
    cpf: str
    cnpj: Optional[str] = None

    @field_validator(field="cpf")
    @classmethod
    def validar_cpf(cls, v) -> str:
        if not v:
            raise Exception("Erro ao criar cliente. Nenhum CPF inserido.")
        v = v.replace(".", "").replace("-", "")
        if len(v) > 11:
            raise Exception("Favor inserir um CPF valido")
        return v

    class Config:
        validate_assignment = True
