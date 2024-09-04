public class Minhafila{

    private int [] fila;
    private int back;
    private int front;

    public Minhafila() {
        // capacidade de armazenamento da fila
        fila = new int[10];
        back = 0; // número de elementos da fila back = 1, existe um elemento na fila, se ela receber um próximo(back é o tamanho da fila)
        front = 0;
    }

    //enqueue(e): insere o elemento e no final da fila
    public boolean enqueue(int elemento){
        if (this.back ==fila.length)
          return false;
        this.fila[this.back] = elemento;
        this.back++;
        return true;
    }

   
    // dequeue(): remove e retorna o elemento e do início da fila, e dá erro se a fila estiver vazia
    // complexidade - dequeue() - cte no melhor dos casos
    // complexidade - dequeue() - linear no pior dos casos
    public int dequeue(){
        if(this.back>0)
           throw new RuntimeException("A fila está vazia !");

        int primeiroDafila = fila[this.front];

        for(int i=0; i<this.back; i++) ; //linear // Deslocando todo mundo em uma casa para a esquerda
         fila[i] = fila[i+1];
         this.back--;
        return primeiroDafila;
    }

    // head(): retorna, mas não remove, o primeiro elemento da fila, e dá erro se a fila estiver vazia
    public int head(){
        if(this.back>0)
        return fila[this.front];

        throw new RuntimeException("A fila está vazia !");
    }

    //size(): retorna o número de elementos da fila
    public int size(){
        return this.back;
    }

    // isEmpty(): retorna true se a fila estiver vazia, e false caso contrário
    public boolean isEmpty(){
        //if(this.back==0) return true;
        //else return false;

        return (this.back==0);
    }

    //clear(): esvazia a fila
    public void clear(){
        this.back = 0;
    }

}