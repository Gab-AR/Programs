package pedroSantosNeto.banco;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;

import org.junit.jupiter.api.Test;

class TesteBanco {

	@Test
	void testarCadastroDeContasJaCadastradas() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");
		Pessoa p2 = new Pessoa(456, "456");

		Conta c1 = new ContaComum(1, p1);
		Conta c2 = new ContaComum(2, p2);
		
		b.cadastrar(c1);
		b.cadastrar(c2);
		
		b.deposito(1, 101);
		assertEquals(101, b.saldo(1), 0.001);
		b.saque(1, 99, "123");
		assertEquals(2, b.saldo(1), 0.001);
		
	}

	@Test
	void testarMovimentacaoDePoupancas() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");
		Pessoa p2 = new Pessoa(456, "456");

		Conta c1 = new ContaComum(1, p1);
		Poupanca c2 = new Poupanca(2, p2);
		
		b.cadastrar(c1);
		b.cadastrar(c2);
		
		b.deposito(1, 101);
		assertEquals(101, b.saldo(1), 0.001);
		b.saque(1, 99, "123");
		assertEquals(2, b.saldo(1), 0.001);
		
		b.deposito(2, 99);
		assertEquals(99, b.saldo(2), 0.001);
		b.saque(2, 99, "456");
		assertEquals(0, b.saldo(2), 0.001);
		
		b.transferencia(1, 2, 2, "123");
		assertEquals(2, b.saldo(2), 0.001);
		assertEquals(0, b.saldo(1), 0.001);
	}
	
	@Test
	void testarRendeJurosPoupancas() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");

		Conta c2 = new Poupanca(2, p1);
		
		b.cadastrar(c2);
		
		b.deposito(2, 100);
		assertEquals(100, b.saldo(2), 0.001);
		b.juros(2, 0.01);
		assertEquals(101, b.saldo(2), 0.001);
	}
	
	@Test
	void testarRendeJurosConta() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");

		Conta c2 = new ContaComum(2, p1);
		
		b.cadastrar(c2);
		
		b.deposito(2, 100);
		assertEquals(100, b.saldo(2), 0.001);
		b.juros(2, 0.01);
		assertEquals(100, b.saldo(2), 0.001);
	}

	@Test
	void testarSaqueContaEspecial() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");

		Conta c2 = new ContaEspecial(2, p1, 100);
		
		b.cadastrar(c2);
		
		b.deposito(2, 100);
		assertEquals(100, b.saldo(2), 0.001);
		// Tentativa de saque com valor negativo: 
		// não deve ser permitido!
		b.saque(2, -1, "123");
		assertEquals(100, b.saldo(2), 0.001);
		// Tentativa de saque com senha errada: 
		// não deve ser permitido!
		b.saque(2, 1, "456");
		assertEquals(100, b.saldo(2), 0.001);
		// Tentativa de saque com valor correto: 
		//  deve ser permitido!
		b.saque(2, 100, "123");
		assertEquals(0, b.saldo(2), 0.001);
		// Tentativa de saque com valor acima do saldo mas dentro do limite: 
		// deve ser permitido!
		b.saque(2, 1, "123");
		assertEquals(-1, b.saldo(2), 0.001);
		// Tentativa de saque com valor acima do saldo e no limite maximo: 
		// deve ser permitido!
		b.saque(2, 99, "123");
		assertEquals(-100, b.saldo(2), 0.001);
		// Tentativa de saque com valor acima do limite: 
		// não deve ser permitido!
		b.saque(2, 0.01, "123");
		assertEquals(-100, b.saldo(2), 0.001);

	}

//	@Test
//	void testarPesquisaPelosLisos() {
//		VetorDeContas v = new VetorDeContas();
//		Banco b = new Banco(v);
//		
//		Pessoa p1 = new Pessoa(123, "123");
//		Pessoa p2 = new Pessoa(456, "456");
//		Pessoa p3 = new Pessoa(789, "789");
//		Pessoa p4 = new Pessoa(111, "111");
//
//		Conta c1 = new ContaComum(1, p1);
//		Conta c2 = new ContaComum(2, p2);
//		ContaComum c3 = new ContaComum(3, p3);
//		ContaComum c4 = new ContaComum(4, p4);
//		
//		b.cadastrar(c1);
//		b.cadastrar(c2);
//		b.cadastrar(c3);
//		b.cadastrar(c4);
//		
//		b.deposito(1, 101);
//		assertEquals(101, b.saldo(1), 0.001);
//		ArrayList<Pessoa> lisos = b.contasZeradas();
//		assertEquals(3, lisos.size());	
//	}
	
	@Test
	void testarSaquesEDepositos() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");
		Pessoa p2 = new Pessoa(456, "456");

		Conta c1 = new ContaComum(1, p1);
		Conta c2 = new ContaComum(2, p2);
		
		b.cadastrar(c1);
		b.cadastrar(c2);
		
		b.deposito(1, 101);
		assertEquals(101, b.saldo(1), 0.001);
		b.saque(1, 99, "123");
		assertEquals(2, b.saldo(1), 0.001);
		// Tentativa de saque com valor negativo:
		// não deve ser permitido.
		b.saque(1, -1, "123");
		assertEquals(2, b.saldo(1), 0.001);
		// Tentativa de saque com senha errada:
		// não deve ser permitido.
		b.saque(1, 1, "456");
		assertEquals(2, b.saldo(1), 0.001);
		// Tentativa de saque com valor maior que o saldo:
		// não deve ser permitido.
		b.saque(1, 10, "123");
		assertEquals(2, b.saldo(1), 0.001);
	}

	@Test
	void testarSaquesEDepositosContasInexistentes() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");
		Pessoa p2 = new Pessoa(456, "456");

		Conta c1 = new ContaComum(1, p1);
		Conta c2 = new ContaComum(2, p2);
		
		b.cadastrar(c1);
		b.cadastrar(c2);
		
		b.deposito(11, 101);
		assertEquals(Banco.INEXISTENTE, b.saldo(11), 0.001);
		b.saque(11, 99, "123");
		assertEquals(-9999999, b.saldo(11), 0.001);
	}
	@Test
	void testarSaldoContaInexistente() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");
		Pessoa p2 = new Pessoa(456, "456");

		Conta c1 = new ContaComum(1, p1);
		Conta c2 = new ContaComum(2, p2);
		
		b.cadastrar(c1);
		b.cadastrar(c2);
		
		b.deposito(1, 101);
		assertEquals(-9999999, b.saldo(11), 0.001);
	}
	
	@Test
	void testarTransferencia() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");
		Pessoa p2 = new Pessoa(456, "456");

		Conta c1 = new ContaComum(1, p1);
		Conta c2 = new ContaComum(2, p2);
		
		b.cadastrar(c1);
		b.cadastrar(c2);
		
		b.deposito(1, 101);
		b.transferencia(1, 2, 100, "123");
		assertEquals(1, b.saldo(1), 0.001);
		assertEquals(100, b.saldo(2), 0.001);
		
		b.transferencia(2, 3, 50, "456");
		assertEquals(100, b.saldo(2), 0.001);

		b.transferencia(5, 2, 50, "456");
		assertEquals(100, b.saldo(2), 0.001);
		
		b.transferencia(2, 1, 100, "123");
		assertEquals(100, b.saldo(2), 0.001);
		System.out.println(ContaComum.quantidade);

   }
	
	@Test
	void testarExtrato() {
		VetorDeContas v = new VetorDeContas();
		Banco b = new Banco(v);
		
		Pessoa p1 = new Pessoa(123, "123");

		Conta c1 = new ContaComum(1, p1);
		
		b.cadastrar(c1);
		
		b.deposito(1, 101);
		b.saque(1, 90, "123");
		b.saque(1, 10, "123");
		b.deposito(1, 9);
		assertEquals(10, b.saldo(1), 0.001);
		String extrato = "Credito: 101.0. Saldo: 101.0\n"
				+ "Debito: 90.0. Saldo: 11.0\n"
				+ "Debito: 10.0. Saldo: 1.0\n"
				+ "Credito: 9.0. Saldo: 10.0\n";
		assertEquals(extrato, b.extrato(1));
		
		assertEquals("", b.extrato(11));

		System.out.println(ContaComum.quantidade);
	}

	@Test
	void testarSaquesEDepositosNovo(){
		ArquivoDeContas v = new ArquivoDeContas("Contas.txt");
		Banco banco = new Banco(v);
	}

}
