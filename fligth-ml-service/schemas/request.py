from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class FligthRequest(BaseModel):
    # ALIAS DEFINE O NOME QUE SERÁ MAPEADO NO JSON. NESSE CASO, O MESMO NOME QUE ESTÁ DEFINIDO NO BACKEND
    companhia: str = Field(alias = "cod_companhia", description="Airline code")
    origem: str = Field(alias = "cod_aeroporto_origem", description="Airport of origin (IATA)")
    destino: str = Field(alias = "cod_aeroporto_destino", description="Destination airport (IATA)")
    data_partida: datetime = Field(alias = "data_hora_partida", description="Date and time of departure in the standard format. ISO-8601")

    model_config = ConfigDict(populate_by_name=True) # CONFIGURAÇÃO PARA ACEITAR JSON COM ALIAS
