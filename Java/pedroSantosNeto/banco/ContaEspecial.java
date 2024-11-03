package pedroSantosNeto.banco;

public class ContaEspecial extends ContaComum {
	
	private double limite;

	public ContaEspecial(int n, Pessoa p, double l) {
		super(n, p);
		limite = l;
	}
	public double getLimite () {
		return limite;
	}
	
	boolean debito(double val, String senha) {
		if (val > 0) {
			if (dono.getSenha() == senha) {
			  if (val <= saldo + limite) {
			    saldo = saldo - val;
			    extrato = extrato + "Debito: " + val + ". Saldo: " + saldo + "\n";
                return true;
			  }
			}
		}
		return false;
	}
	

}
