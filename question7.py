def create_handlers(callback):
   handlers = []
   for step in range(5):
      # добавляем обработчики для каждого шага (от 0 до 4)
      # проблема в том что "step" локально будет равен последнему значению   
      handlers.append(lambda step: callback(step))
   return handlers

def execute_handlers(handlers):
  # запускаем добавленные обработчики (шаги от 0 до 4)
  for handler in range(len(handlers)):
     print(handlers[handler](handler))

handlers = create_handlers(lambda x: x**2)
execute = execute_handlers(handlers)
