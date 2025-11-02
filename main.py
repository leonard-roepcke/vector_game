import drawing
import enemy
import vector
import inputs
app = drawing.PygameApp()
enemy_handler = enemy.EnemyHandler(app)
vector_handler = vector.VectorHandler(app)
input_handler = inputs.InputHandler(app)

while app.loop():
    app.draw_coordinates()
    enemy_handler.update_enemys()
    vector_handler.update_vectors()
    vect = input_handler.update()
    if vect != None:
        vector_handler.add_vector(vect)