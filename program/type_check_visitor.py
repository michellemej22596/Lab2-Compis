from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
      left_type = self.visit(ctx.expr(0))
      right_type = self.visit(ctx.expr(1))
      if isinstance(left_type, StringType) and isinstance(right_type, IntType):
          raise TypeError(f"Cannot add a string and an integer.")
      return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    if isinstance(left_type, BoolType) or isinstance(right_type, BoolType):
        raise TypeError(f"Cannot perform arithmetic operations with booleans.")
    return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

  def visitVarDeclaration(self, ctx: SimpleLangParser.VarDeclarationContext):
    var_name = ctx.ID().getText()
    if var_name not in self.types:
        raise TypeError(f"Variable {var_name} is used before it is declared.")
    return self.types.get(var_name, None)
