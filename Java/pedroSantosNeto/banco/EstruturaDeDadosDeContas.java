package pedroSantosNeto.banco;

public interface EstruturaDeDadosDeContas {
    public abstract void cadastrar(Conta c);
		
	public abstract Conta pesquisar(int num);
}
