package ec.ups.edu.modelo;

public class Persona {
private int cedula;
private int codigo;
private String nombre;
private String apellido;

    public Persona(int cedula, int codigo, String nombre, String apellido) {
        this.cedula = cedula;
        this.codigo = codigo;
        this.nombre = nombre;
        this.apellido = apellido;
    }

    public Persona() {
    }

    public int getCedula() {
        return cedula;
    }

    public void setCedula(int cedula) {
        this.cedula = cedula;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "Persona{" + "cedula=" + cedula + ", codigo=" + codigo + ", nombre=" + nombre + ", apellido=" + apellido + '}';
    }

}
