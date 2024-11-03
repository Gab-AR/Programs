package pedroSantosNeto.banco;

public class Poupanca extends ContaComum {
	
	public Poupanca (int n, Pessoa p) {
		super (n, p);
	}    
	
	public void rendeJuros(Double taxa) {
	    credito(saldo * taxa);
	}
}	
	
