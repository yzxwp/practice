"""
多种事件绑定方式汇总
组件对象绑定
  1. 通过command方式绑定属性绑定(适合简单不需要获取event对象)
  2. 通过bind()方法绑定(适合需要获取event对象)
组件类绑定
  调用对象的bind_class()函数, 将该组件类所有的组件绑定事件: w.bind_class('Wiget', 'event', eventhanler)

"""