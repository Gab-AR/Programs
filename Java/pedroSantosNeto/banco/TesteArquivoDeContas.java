package pedroSantosNeto.banco;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

class TesteArquivoDeContas {
    private static final String ARQUIVO_TESTE = "contas_teste.txt";
    private ArquivoDeContas arquivoContas;
    private Banco banco;

    @BeforeEach
    void setUp() {
        // Cria um novo arquivo de contas para cada teste
        arquivoContas = new ArquivoDeContas(ARQUIVO_TESTE);
        banco = new Banco(arquivoContas);
    }

    @AfterEach
    void tearDown() {
        // Limpa o arquivo após cada teste
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
        assertEquals(0, contaPesquisada.getSaldo());
        assertEquals(123, contaPesquisada.getDono().getCpf());
    }

    @Test
    void testeMultiplasConta() {
        // Cadastra múltiplas contas
        Pessoa p1 = new Pessoa(123, "senha123");
        Pessoa p2 = new Pessoa(456, "senha456");
        Pessoa p3 = new Pessoa(789, "senha789");

        Conta c1 = new ContaComum(1, p1);
        Conta c2 = new ContaEspecial(2, p2, 1000);
        Conta c3 = new Poupanca(3, p3);

        banco.cadastrar(c1);
        banco.cadastrar(c2);
        banco.cadastrar(c3);

        // Verifica se todas as contas foram salvas corretamente
        assertNotNull(arquivoContas.pesquisar(1));
        assertNotNull(arquivoContas.pesquisar(2));
        assertNotNull(arquivoContas.pesquisar(3));
    }

    @Test
    void testeOperacoesContaArquivo() {
        Pessoa p1 = new Pessoa(123, "senha123");
        Conta c1 = new ContaComum(1, p1);
        
        banco.cadastrar(c1);
        
        // Realiza operações
        banco.deposito(1, 100);
        assertEquals(100, banco.saldo(1));

        banco.saque(1, 30, "senha123");
        assertEquals(70, banco.saldo(1));

        // Verifica se as operações foram persistidas
        Conta contaPesquisada = arquivoContas.pesquisar(1);
        assertEquals(70, contaPesquisada.getSaldo());
    }

    @Test
    void testePesquisaContaInexistente() {
        assertNull(arquivoContas.pesquisar(999));
    }

    @Test
    void testeTransferenciaEntreContas() {
        Pessoa p1 = new Pessoa(123, "senha123");
        Pessoa p2 = new Pessoa(456, "senha456");
        
        Conta c1 = new ContaComum(1, p1);
        Conta c2 = new ContaComum(2, p2);
        
        banco.cadastrar(c1);
        banco.cadastrar(c2);
        
        banco.deposito(1, 100);
        banco.transferencia(1, 2, 50, "senha123");

        assertEquals(50, banco.saldo(1));
        assertEquals(50, banco.saldo(2));

        // Verifica se as transferências foram persistidas
        Conta conta1 = arquivoContas.pesquisar(1);
        Conta conta2 = arquivoContas.pesquisar(2);
        
        assertEquals(50, conta1.getSaldo());
        assertEquals(50, conta2.getSaldo());
    }

    @Test
    void testeContaEspecialArquivo() {
        Pessoa p1 = new Pessoa(123, "senha123");
        ContaEspecial c1 = new ContaEspecial(1, p1, 1000);
        
        banco.cadastrar(c1);
        
        banco.deposito(1, 100);
        banco.saque(1, 200, "senha123"); // Saque maior que o saldo, mas dentro do limite

        Conta contaPesquisada = arquivoContas.pesquisar(1);
        assertEquals(-100, contaPesquisada.getSaldo());
    }

    @Test
    void testePoupancaArquivo() {
        Pessoa p1 = new Pessoa(123, "senha123");
        Poupanca c1 = new Poupanca(1, p1);
        
        banco.cadastrar(c1);
        
        banco.deposito(1, 100);
        banco.juros(1, 0.1); // 10% de juros

        Conta contaPesquisada = arquivoContas.pesquisar(1);
        assertEquals(110, contaPesquisada.getSaldo());
    }

    @Test
    void testeExtrato() {
        Pessoa p1 = new Pessoa(123, "senha123");
        Conta c1 = new ContaComum(1, p1);
        
        banco.cadastrar(c1);
        
        banco.deposito(1, 100);
        banco.saque(1, 30, "senha123");
        banco.deposito(1, 50);

        String extrato = banco.extrato(1);
        assertTrue(extrato.contains("Credito: 100.0"));
        assertTrue(extrato.contains("Debito: 30.0"));
        assertTrue(extrato.contains("Credito: 50.0"));
    }

    @Test
    void testePersistenciaDados() {
        // Primeiro cria e salva uma conta
        Pessoa p1 = new Pessoa(123, "senha123");
        Conta c1 = new ContaComum(1, p1);
        banco.cadastrar(c1);
        banco.deposito(1, 100);

        // Cria uma nova instância do banco com o mesmo arquivo
        ArquivoDeContas novoArquivoContas = new ArquivoDeContas(ARQUIVO_TESTE);
        Banco novoBanco = new Banco(novoArquivoContas);

        // Verifica se os dados persistiram
        assertEquals(100, novoBanco.saldo(1));
    }
}
