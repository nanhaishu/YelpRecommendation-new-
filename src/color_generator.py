from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time


def fetch_colors(hex_color):
    """从[mycolor.space](https://mycolor.space)获取颜色调色板的HEX值。

    Args:
        hex_color (str): 要查询的HEX颜色代码。

    Returns:
        dict: 包含颜色调色板名称和对应HEX颜色值的字典。

        1. `Generic Gradient`（通用渐变）- 从浅色到鲜艳色彩的基本渐变调色板。
        2. `Matching Gradient`（匹配渐变）- 提供平滑渐变的颜色，常用于细腻且专业的外观。
        3. `Spot Palette`（点缀调色板）- 一系列关键色彩的选择，可能用于突出重要元素。
        4. `Twisted Spot Palette`（扭曲点缀调色板）- 点缀调色板的变体，颜色选择带有变化。
        5. `Classy Palette`（优雅调色板）- 优雅而精致的色彩，适合豪华设计。
        6. `Cube Palette`（立方调色板）- 简约且极简主义的，常使用少量颜色以达到干净的外观。
        7. `Switch Palette`（切换调色板）- 用于具有开/关状态的界面，使用对比色。
        8. `Small Switch Palette`（小型切换调色板）- 切换调色板的小型版本，变化较少。
        9. `Skip Gradient`（跳跃渐变）- 一种跳跃式的鲜艳渐变调色板。
        10. `Natural Palette`（自然调色板）- 唤起自然、平静感觉的颜色，通常是柔和的粉彩色。
        11. `Matching Palette`（协调调色板）- 相互搭配得很好的颜色，创造和谐的外观。
        12. `Squash Palette`（蔬菜调色板）- 混合了泥土色和水色调，表现出元素的平衡。
        13. `Grey Friends`（灰色之友）- 各种灰色阴影，提供单色外观。
        14. `Dotting Palette`（点缀调色板）- 玩味十足，可能用于点状图案。
        15. `Skip Shade Gradient`（轻盈跳跃渐变）- 一种轻盈通透的渐变，理想用于清新外观。
        16. `Threedom`（自由三色）- 三种协调良好的颜色，暗示设计的自由。
        17. `Highlight Palette`（高亮调色板）- 设计用于突出设计中的关键特征的颜色。
        18. `Neighbor Palette`（邻近调色板）- 色调接近的颜色，创造出协调的外观。
        19. `Discreet Palette`（内敛调色板）- 细腻且低调的颜色，适用于柔和的背景或布局。
        20. `Dust Palette`（尘埃调色板）- 尘埃或柔和的色调，适合复古或怀旧风格。
        21. `Collective`（集体调色板）- 一组互补色彩，适用于团队或群体主题。
        22. `Friend Palette`（友好调色板）- 友好且吸引人的色彩，充满活力。
        23. `Pin Palette`（定位调色板）- 锐利且精确的色彩，可能用于地图或信息图表。
        24. `Shades`（阴影渐变）- 从同一种颜色的渐变色调，创造深度。
        25. `Random Shades`（随机阴影） - 随机搭配的色调，营造出动感外观。
    """
    driver = webdriver.Safari()  # 使用Safari浏览器
    url = f"https://mycolor.space/?hex=%23{hex_color}&sub=1"  # 构建目标URL
    driver.get(url)  # 打开网页
    time.sleep(5)  # 等待网页加载

    color_data = {hex_color: {}}  # 初始化存储颜色数据的字典

    # 抓取页面上所有颜色调色板
    palettes = driver.find_elements(By.CLASS_NAME, 'color-palette')
    for palette in palettes:
        palette_name = palette.find_element(By.TAG_NAME, 'h2').text  # 获取调色板的名称
        colors = []  # 存放调色板的颜色值
        color_boxes = palette.find_elements(By.CLASS_NAME, 'color-box')
        for color_box in color_boxes:
            hex_value = color_box.find_element(
                By.TAG_NAME, 'input').get_attribute('value')  # 获取HEX值
            colors.append(hex_value)
        color_data[hex_color][palette_name] = colors  # 将调色板存储到字典

    driver.quit()  # 关闭浏览器
    return color_data


def append_to_json_file(data, file_path='color.json'):
    """将数据追加到JSON文件中。

    Args:
        data (dict): 要追加的数据。
        file_path (str, optional): JSON文件的路径。默认为'color.json'.
    """
    try:
        # 尝试打开并读取现有数据
        with open(file_path, 'r') as file:
            content = file.read()
            if content:  # 检查文件内容是否为空
                file_data = json.loads(content)
            else:
                file_data = {}
    except FileNotFoundError:
        file_data = {}

    # 更新数据
    for key, value in data.items():
        if key in file_data:
            file_data[key].update(value)
        else:
            file_data[key] = value

    # 写入更新后的数据
    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=2, sort_keys=True)


if __name__ == "__main__":
    hex_color = 'E5E5E5'  # 要查询的HEX颜色代码
    result = fetch_colors(hex_color)
    append_to_json_file(result, '../assets/color.json')  # 追加结果到JSON文件
