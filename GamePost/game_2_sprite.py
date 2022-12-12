"""
2019.11.29 19:51
精灵
图像加载、位置保存、绘制图像 => 简化出 精灵、精灵组

pygame.sprite.Sprite 类 (需要派生子类):
image 记录图像数据
rect 记录位置
update(*args) 更新精灵位置
kill() 从所有组中删除

pygame.sprite.Group 类 精灵组：
__init__(self, *Sprite)
add(*sprites) 向组中增加精灵
sprites() 返回所有精灵列表
update(*args) 让组中所有精灵调用update()方法
draw(Surface) 将组中所有精灵的 image 绘制到 Surface 的 Rect 位置

对于精灵的操作
游戏初始化：
    创建精灵，创建精灵组
游戏循环：
    精灵组.update()，精灵组.draw(screen)，pygame.display.update()


"""