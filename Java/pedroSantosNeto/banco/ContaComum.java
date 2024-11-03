package pedroSantosNeto.banco;


public class ContaComum extends Conta {
	

	public ContaComum (int n, Pessoa p) {
       super(n, p);
	}
		
	boolean debito(double val, String senha) {
		if (val > 0) {
			if (dono.getSenha() == senha) {
			  if (val <= saldo) {
			    saldo = saldo - val;
			    extrato = extrato + "Debito: " + val + ". Saldo: " + saldo + "\n";
                return true;
			  }
			}
		}
		return false;
	}
}
