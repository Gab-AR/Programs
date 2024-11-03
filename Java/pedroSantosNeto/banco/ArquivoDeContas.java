package pedroSantosNeto.banco;

import java.io.*;
import java.util.*;

public class ArquivoDeContas implements EstruturaDeDadosDeContas {
    private String nomeArquivo;

    public ArquivoDeContas(String nomeArquivo) {
        this.nomeArquivo = nomeArquivo;
    }

    @Override
    public void cadastrar(Conta c) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(nomeArquivo, true))) {
            writer.println(serializarConta(c));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public Conta pesquisar(int num) {
        try (BufferedReader reader = new BufferedReader(new FileReader(nomeArquivo))) {
            String linha;
            while ((linha = reader.readLine()) != null) {
                Conta c = deserializarConta(linha);
                if (c != null && c.getNumero() == num) {
                    return c;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    private String serializarConta(Conta c) {
        String tipo = "CC"; // ContaComum
        String extra = "";
        if (c instanceof ContaEspecial) {
            tipo = "CE";
            extra = "," + ((ContaEspecial)c).getLimite();
        } else if (c instanceof Poupanca) {
            tipo = "CP";
        }
        return tipo + "," + c.getNumero() + "," + c.getSaldo() + "," + c.getDono().getCpf() + "," + c.getDono().getSenha() + extra;
    }

    private Conta deserializarConta(String linha) {
        String[] partes = linha.split(",");
        if (partes.length >= 5) {
            String tipo = partes[0];
            int numero = Integer.parseInt(partes[1]);
            double saldo = Double.parseDouble(partes[2]);
            int cpf = Integer.parseInt(partes[3]);
            String senha = partes[4];
            Pessoa p = new Pessoa(cpf, senha);
            Conta c;
            switch (tipo) {
                case "CE":
                    double limite = Double.parseDouble(partes[5]);
                    c = new ContaEspecial(numero, p, limite);
                    break;
                case "CP":
                    c = new Poupanca(numero, p);
                    break;
                default:
                    c = new ContaComum(numero, p);
            }
            c.credito(saldo);
            return c;
        }
        return null;
    }

    public void atualizar(Conta c) {
        List<String> linhas = new ArrayList<>();
        boolean encontrou = false;
        try (BufferedReader reader = new BufferedReader(new FileReader(nomeArquivo))) {
            String linha;
            while ((linha = reader.readLine()) != null) {
                Conta contaExistente = deserializarConta(linha);
                if (contaExistente != null && contaExistente.getNumero() == c.getNumero()) {
                    linhas.add(serializarConta(c));
                    encontrou = true;
                } else {
                    linhas.add(linha);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    
        if (!encontrou) {
            linhas.add(serializarConta(c));
        }
    
        try (PrintWriter writer = new PrintWriter(new FileWriter(nomeArquivo))) {
            for (String linha : linhas) {
                writer.println(linha);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}