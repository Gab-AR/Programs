package pedroSantosNeto.banco;

import java.util.ArrayList;

public class Banco {
	
	public static final int INEXISTENTE = -9999999;

	// private VetorDeContas contas = new VetorDeContas();
	private EstruturaDeDadosDeContas contas;	
	
	public Banco(EstruturaDeDadosDeContas contas) {
		this.contas = contas;
	}
	
	public void cadastrar(Conta c) {
		contas.cadastrar(c);
	}
	
//	public ArrayList<Pessoa> contasZeradas(){
//		EstruturaDeDadosDeContas atual = contas;
//		ArrayList<Pessoa> lisos = new ArrayList<Pessoa>();
//		
//		while (atual.getConta() != null) {
//			if (atual.getConta().getSaldo() == 0) {
//				lisos.add(atual.getConta().getDono());
//			}
//			atual = atual.getProx();
//		}
//		System.out.println(lisos);
//		return lisos;
//	}
	
public void saque(int num, double val, String senha) {
    Conta c = contas.pesquisar(num);
    if (c != null && c.getDono().getSenha().equals(senha)) {
        if (c.debito(val, senha)) {
            ((ArquivoDeContas)contas).atualizar(c);
        }
    }
}
	
	public void juros(int num, double tx) {
		Conta c = contas.pesquisar(num);
		if (c != null && c instanceof Poupanca p) {
			p.rendeJuros(tx);
		}
	}
	
	public void deposito(int num, double val) {
		Conta c = contas.pesquisar(num);
		if (c != null) {
			c.credito(val);
			((ArquivoDeContas)contas).atualizar(c);
		}
	}
	
	public String extrato(int num) {
		Conta c = contas.pesquisar(num);
		if (c != null) {
		  return c.getExtrato();
		}
		return "";
	}
	
	public double saldo(int num) {
		Conta c = contas.pesquisar(num);
		if (c != null) {
		  return c.getSaldo();
		}
		return INEXISTENTE;
	}
	

	
	public void transferencia(int num1, int num2, double val, String senha) {
		Conta c1 = contas.pesquisar(num1);
		Conta c2 = contas.pesquisar(num2);
		if (c1 != null && c2 != null) {
			if (c1.debito(val, senha)) {
				c2.credito(val);
				((ArquivoDeContas)contas).atualizar(c1);
				((ArquivoDeContas)contas).atualizar(c2);
			}
		}
	}
}
