.data
.include "imagem_qcif_r.asm"

# Vetor de 256 palavras (1 palavra por valor de pixel)
histograma: .word 0:256

# Mensagens
msg_pixel:      .string "Pixel "
msg_ocorrencia: .string " - Ocorrencia "
newline:        .string "\n"
.text
.globl main

main:
    la t0, imagem         # t0 = endereço do início da imagem
    li t1, 25344          # número total de pixels (176x144)
    la t2, histograma     # t2 = endereço do histograma

    # Loop para contar as ocorrências dos pixels
loop_pixels:
    beqz t1, imprime_histograma   # se t1 == 0, acabou

    lbu t3, 0(t0)       # lê byte (valor do pixel)
    addi t0, t0, 1     # próximo pixel
    slli t4, t3, 2     # índice * 4 (palavra de 4 bytes)
    add t5, t2, t4     # endereço do histograma[t3]
    lw t6, 0(t5)       # carrega valor atual do histograma
    addi t6, t6, 1     # incrementa contagem
    sw t6, 0(t5)       # salva de volta
    addi t1, t1, -1    # decrementa contador de pixels
    j loop_pixels

# Imprime valores não zero do histograma
imprime_histograma:
    li s0, 0           # contador do índice do pixel
    la t2, histograma

loop_impressao:
    li s1, 256
    beq s0, s1, fim    # terminou todos os 256 valores

    slli s2, s0, 2     # t9 = t7 * 4
    add s3, t2, s2    # t10 = endereço de histograma[t7]
    lw s4, 0(s3)     # t11 = histograma[t7]

    beqz s4, proximo_pixel  # se zero, não imprime

    # Imprime "Pixel "
    li a7, 4
    la a0, msg_pixel
    ecall

    # Imprime o valor do pixel (t7)
    li a7, 1
    mv a0, s0
    ecall

    # Imprime " - Acorrencia "
    li a7, 4
    la a0, msg_ocorrencia
    ecall

    # Imprime a contagem (t11)
    li a7, 1
    mv a0, s4
    ecall

    # Imprime nova linha
    li a7, 4
    la a0, newline
    ecall

proximo_pixel:
    addi s0, s0, 1
    j loop_impressao

fim:
    li a7, 10
    ecall