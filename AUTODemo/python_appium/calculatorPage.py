#encoding:utf-8
class CalculatorPage():
    def __init__(self,driver):
        self.driver=driver

    @property
    def button1(self):
        element=self.driver.find_element_by_id("com.android.calculator2:id/digit_1")
        return element
    @property
    def button2(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_2")
        return element
    @property
    def button3(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_3")
        return element
    @property
    def button4(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_4")
        return element
    @property
    def button5(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_5")
        return element
    @property
    def button6(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_6")
        return element
    @property
    def button7(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_7")
        return element
    @property
    def button8(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_8")
        return element
    @property
    def button9(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_9")
        return element
    @property
    def button0(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/digit_0")
        return element
    @property
    def button_jia(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/op_add")
        return element
    @property
    def button_jian(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/op_sub")
        return element
    @property
    def button_cheng(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/op_mul")
        return element
    @property
    def button_chu(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/op_div")
        return element
    @property
    def button_clear(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/op_clr")
        return element
    @property
    def button_dengyu(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/eq")
        return element

    @property
    def button_text(self):
        element = self.driver.find_element_by_id("com.android.calculator2:id/formula")
        text=element.text
        return text