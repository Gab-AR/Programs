package pedroSantosNeto.banco;

public class ContaImposto extends Conta {
	
	private double imposto;

	public ContaImposto(int n, Pessoa p, double i) {
		super(n, p);
		imposto = i;
	}
	
	boolean debito(double val, String senha) {
		if (val > 0) {
			if (dono.getSenha() == senha) {
			  if (val + saldo * imposto <= saldo) {
			    saldo = saldo - (val + saldo * imposto);
			    extrato = extrato + "Debito: " + (val + + saldo * imposto) + ". Saldo: " + saldo + "\n";
                return true;
			  }
			}
		}
		return false;
	}
}
