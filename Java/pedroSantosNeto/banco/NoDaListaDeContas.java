package pedroSantosNeto.banco;

public class NoDaListaDeContas implements EstruturaDeDadosDeContas {
	
	private Conta conta = null;
	private NoDaListaDeContas prox = null;
	
	public void cadastrar(Conta c) {
		if (conta == null) {
			conta = c;
			prox = new NoDaListaDeContas();
		} else {
			prox.cadastrar(c);
		}
	}

	public Conta pesquisar(int num) {
		if (conta == null) {
			return null;
		}
		if (conta.getNumero() == num) {
			return conta;
		} else {
			return prox.pesquisar(num);
		}
	}

	public Conta getConta() {
		return conta;
	}

	public NoDaListaDeContas getProx() {
		return prox;
	}
}
