package pedroSantosNeto.banco;

import java.util.*;

public class UsoDeConta {

	public static void main(String[] args) {
		
		Date hoje = new Date();
		System.out.println(hoje);
		
		int dia = hoje.getDate();
		int mes = hoje.getMonth();
		int ano = hoje.getYear();
		int semana = hoje.getDay();
		long milis = hoje.getTime();
		
		System.out.println("Dia: " + dia);
		System.out.println("Mes: " + mes);
		System.out.println("Ano: " + ano);
		System.out.println("Semana: " + semana);
		System.out.println("Milis: " + milis);
		
		Date outra = new Date(0);
		System.out.println(outra);
		
		System.out.println("Outra antes? " + outra.before(hoje));
		
		int a = GregorianCalendar.DAY_OF_MONTH;
		
		GregorianCalendar gc = new GregorianCalendar();
		gc.set(1974,  10, 14, 7, 15);
		Date maisUma = gc.getTime();
		long milisGC = gc.getTimeInMillis();
		
		GregorianCalendar gc2 = new GregorianCalendar();
		
		System.out.println(gc2.before(gc));
		
		System.out.println("Dia: " + gc.get(GregorianCalendar.DAY_OF_MONTH)); 
		System.out.println("Mes: " +gc.get(GregorianCalendar.MONTH)); 
		System.out.println("Ano: " +gc.get(GregorianCalendar.YEAR));
		System.out.println("Hora: " +gc.get(GregorianCalendar.HOUR));
		System.out.println("Min: " +gc.get(GregorianCalendar.MINUTE));
		System.out.println("Segundo: " +gc.get(GregorianCalendar.SECOND));
		System.out.println("Milis: " +gc.get(GregorianCalendar.MILLISECOND));		

		
//		
//		ArrayList<Pessoa> pessoas = new ArrayList<Pessoa>();
//		
//		Pessoa p1 = new Pessoa(123, "password");
//		p1.setNome("Pedro");
//		
//		Pessoa p2 = new Pessoa(456, "password");
//		p2.setNome("Raimundo");
//		
//		pessoas.add(p1);
//		pessoas.add(p2);
//		
//		System.out.println(pessoas.size());
//		
//		for (Pessoa pessoa : pessoas) {
//			if (pessoa.getCpf() == 123) {
//				// faça algo
//			}
//		}
//		
//		Conta c = new Conta(1, p1);
//		Conta c1 = new Conta(2, p2);
//		Conta c2 = c1;
//		
//		c.credito(100);
//		c.credito(-100);
//		c.debito(-10, "password");
//		c.debito(10, "password");
//		
//		c1.credito(101);
//		c2.debito(101, "passwd");
//				
//		System.out.println("Dono: " + c.getDono().getNome() + ". Conta: " + c.getNumero() + ".\n" + c.getExtrato() );
//		System.out.println("Dono: " + c1.getDono().getNome() + ". Conta: " + c1.getNumero() + ".\n" + c1.getExtrato() );
	}
}
