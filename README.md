# 🏨 Sistema de Gerenciamento de Reservas - Refúgio dos Sonhos

Este projeto foi desenvolvido como parte de um estudo de **Programação Orientada a Objetos (POO)** em Python, com integração da biblioteca **Flet** para criar uma interface gráfica interativa.

---

## 🎯 Objetivos do Projeto
- Aplicar conceitos de **POO**: herança, polimorfismo e encapsulamento.
- Criar um sistema modular para gerenciar **clientes, quartos e reservas**.
- Implementar uma interface gráfica simples e funcional com **Flet**.

---

## 🧩 Estrutura das Classes

### Pessoa (Classe Base)
- Atributos: `nome`, `telefone`, `email` (privados).
- Métodos:
  - Getters e setters com validação.
  - `exibir_informacoes()` → retorna dados básicos da pessoa.

### Cliente (Herança de Pessoa)
- Atributos: `id_unico` (privado).
- Métodos:
  - `get_id()`
  - Sobrescreve `exibir_informacoes()` para incluir ID.

### Quarto
- Atributos: `numero`, `tipo`, `preco_diaria`, `disponivel` (privados).
- Métodos:
  - `reservar()`, `liberar()`
  - `is_disponivel()`
  - `exibir_informacoes()` → mostra status do quarto.

### Reserva
- Atributos: `cliente`, `quarto`, `check_in`, `check_out`, `status` (privados).
- Métodos:
  - `cancelar()`
  - `exibir_informacoes()` → mostra detalhes da reserva.

### GerenciadorDeReservas
- Responsável por centralizar operações:
  - `adicionar_cliente()`
  - `adicionar_quarto()`
  - `criar_reserva()`
  - `listar_reservas()`, `listar_quartos()`, `listar_clientes()`

---

## 🔑 Conceitos Aplicados

### Encapsulamento
- Atributos sensíveis (`__atributo`) são privados.
- Métodos públicos (getters/setters) controlam acesso e validam dados.

### Herança
- `Cliente` herda de `Pessoa`, reutilizando atributos comuns.

### Polimorfismo
- Método `exibir_informacoes()` é definido em `Pessoa` e sobrescrito em `Cliente`.
- Também utilizado em `Quarto` e `Reserva` para exibir informações específicas.

---

## 🎨 Interface Gráfica (Flet)

A interface inclui:
- **Lista de quartos** com status de disponibilidade.
- **Formulário de reserva**:
  - Seleção de cliente.
  - Seleção de quarto.
  - Datas de check-in e check-out.
- **Lista de reservas** com opção de **cancelar**.

---

## 🚀 Como executar

1. Instale dependências:
   ```bash
   pip install flet
