import drawing
import enemy
import vector
app = drawing.PygameApp()
enemy_handler = enemy.EnemyHandler(app)
vector_handler = vector.VectorHandler(app)
vector_handler.add_vector((4,5))
while app.loop():
    app.draw_coordinates()
    enemy_handler.update_enemys()
    vector_handler.update_vectors()
    
    