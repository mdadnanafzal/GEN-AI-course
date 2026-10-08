class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strngth = strength
#code duplication 
# class GingerChai(chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level

# ecplicit call 
# class GingerChai(chai):
#     def __init__(self, type_, strength, spice_level):
#         chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

#using super methis
class GingerChai(chai):
    def __init__(self, type_, strength):
        super().__init__(type_, strength)
        self.spice_level = spice_level

