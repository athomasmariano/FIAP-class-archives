package org.example;

import lombok.*;

import java.util.Objects;
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Carta {
    @DataField(prompt = "Nome da Carta")
    private String nome;

    @DataField(prompt = "Texto da Carta")
    private String texto;

    @DataField(prompt = "Artista da carta")
    private String artista;


}


