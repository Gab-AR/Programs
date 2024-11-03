package pedroSantosNeto.banco;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

class Teste2 {
    private static final String ARQUIVO_TESTE = "contas_teste.txt";
    private ArquivoDeContas arquivoContas;
    private Banco banco;

    @BeforeEach
    void setUp() {
        arquivoContas = new ArquivoDeContas(ARQUIVO_TESTE);
        banco = new Banco(arquivoContas);
    }

    @AfterEach
    void tearDown() {
        try {
            Files.deleteIfExists(Paths.get(ARQUIVO_TESTE));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Test
    void testeCadastroContaComum() {
        Pessoa p1 = new Pessoa(123, "senha123");
        Conta c1 = new ContaComum(1, p1);
        
        banco.cadastrar(c1);
        
        Conta contaPesquisada = arquivoContas.pesquisar(1);
        assertNotNull(contaPesquisada);
        assertEquals(1, contaPesquisada.getNumero());
    }

    @Test
    void testeOperacoesBasicas() {
        // Teste simplificado de operações básicas
        Pessoa p1 = new Pessoa(123, "senha123");
        Conta c1 = new ContaComum(1, p1);
        
        banco.cadastrar(c1);
        
        // Teste de depósito
        banco.deposito(1, 100);
        assertEquals(100, arquivoContas.pesquisar(1).getSaldo(), 0.001);
        
        // Teste de saque
        banco.saque(1, 50, "senha123");
        assertEquals(50, arquivoContas.pesquisar(1).getSaldo(), 0.001);
    }

    @Test
    void testePesquisaContaInexistente() {
        assertNull(arquivoContas.pesquisar(999));
    }

    @Test
    void testeTransferenciaSimples() {
        Pessoa p1 = new Pessoa(123, "senha123");
        Pessoa p2 = new Pessoa(456, "senha456");
        
        Conta c1 = new ContaComum(1, p1);
        Conta c2 = new ContaComum(2, p2);
        
        banco.cadastrar(c1);
        banco.cadastrar(c2);
        
        banco.deposito(1, 100);
        banco.transferencia(1, 2, 50, "senha123");

        assertEquals(50, arquivoContas.pesquisar(1).getSaldo(), 0.001);
        assertEquals(50, arquivoContas.pesquisar(2).getSaldo(), 0.001);
    }

    @Test
    void testeContaEspecialSimples() {
        Pessoa p1 = new Pessoa(123, "senha123");
        ContaEspecial c1 = new ContaEspecial(1, p1, 100);
        
        banco.cadastrar(c1);
        banco.deposito(1, 50);
        
        assertEquals(50, arquivoContas.pesquisar(1).getSaldo(), 0.001);
    }

    @Test
    void testePoupancaSimples() {
        Pessoa p1 = new Pessoa(123, "senha123");
        Poupanca c1 = new Poupanca(1, p1);
        
        banco.cadastrar(c1);
        banco.deposito(1, 100);
        
        assertEquals(100, arquivoContas.pesquisar(1).getSaldo(), 0.001);
    }

    @Test
    void testeExtratoSimples() {
        Pessoa p1 = new Pessoa(123, "senha123");
        Conta c1 = new ContaComum(1, p1);
        
        banco.cadastrar(c1);
        banco.deposito(1, 100);
        
        String extrato = banco.extrato(1);
        assertTrue(extrato.contains("Credito: 100.0"));
    }

    @Test
    void testePersistenciaDados() {
        // Teste de persistência básica
        Pessoa p1 = new Pessoa(123, "senha123");
        Conta c1 = new ContaComum(1, p1);
        banco.cadastrar(c1);
        banco.deposito(1, 100);

        // Cria nova instância para verificar persistência
        ArquivoDeContas novoArquivoContas = new ArquivoDeContas(ARQUIVO_TESTE);
        Conta contaRecuperada = novoArquivoContas.pesquisar(1);
        
        assertNotNull(contaRecuperada);
        assertEquals(100, contaRecuperada.getSaldo(), 0.001);
    }
}