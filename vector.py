from math import acos,pi
class Vector:
    def __init__(self,coords):
        self.coords = coords
    def __add__(v1 , v2):
        ''' Adds two vectors each dimention with its equivilant'''
        if len(v1.coords) != len(v2.coords):
            '''The validation of dimensions number'''
            raise ValueError('The added vectors don\'t have the same dimension number')
        result =[0]*len(v1.coords)
        for i in range(len(v1.coords)):
            result[i] = v1.coords[i]+v2.coords[i]
        return result
    def __sub__(v1 , v2):
        ''' Adds two vectors each dimention with its equivilant'''
        if len(v1.coords) != len(v2.coords):
            '''The validation of dimensions number'''
            raise ValueError('The added vectors don\'t have the same dimension number')
        result =[0]*len(v1.coords)
        for i in range(len(v1.coords)):
            result[i] = v1.coords[i]-v2.coords[i]
        return result
    def __mul__(v1,v2):
        '''This function returns the dot product of two vectors '''
        if len(v1.coords) != len(v2.coords):
            '''The validation of dimensions' number'''
            raise ValueError('The added vectors don\'t have the same dimension number')

        '''To determine using dot product or a scalar multiplying'''
        if (type(v2.coords) ==type([])) and (type(v2.coords)==type([])):
            result = 0
            for i in range(len(v1.coords)):
                result += v1.coords[i]*v2.coords[i]
        '''To determine using left or right scalar multiplying'''
            
        elif type(v2) in [type(0.0) ,type(0)] :
            for i in range(len(v1.coords)):
                result += v1.coords[i]*v2
        elif type(v1) in [type(0.0) ,type(0)] :
            for i in range(len(v1.coords)):
                result += v2.coords[i]*v1
        return result
    def cross_product(v1,v2):
        '''Returns the cross product of two vectors of three dimensions'''
        result = [0]*len(v1.coords)
        '''The validation of dimensions' number'''
        if len(v1.coords) != len(v2.coords) != 3:
            raise ValueError('The added vectors don\'t have the same dimension number')
        '''result here is identifier of the matrix consists of origins row ,v1 row and v2 row'''
        result = Vector([v1.coords[1]*v2.coords[2] - v1.coords[2]*v2.coords[1] , -(v1.coords[0]*v2.coords[2] - v1.coords[2]*v2.coords[0]),v1.coords[1]*v2.coords[2] - v1.coords[2]*v2.coords[1]])
        return result
    def magnitude(v):
        '''Returns the magnitude of one vector'''
        result = 0
        '''magnitude =squre root of(i**2+j**2...)'''
        for i in range(len(v.coords)):
            result += v.coords[i]**2
        result = result ** 0.5
        return result
    def get_uv (v):
        '''Returns the unit vector of one vector'''
        uv = [0]*len(v.coords)
        for i in range(len(v.coords)):
           uv[i]= Vector(v.coords[i]/ v.magnitude(v))
        return uv
    def angles(v):
        '''Returns the angles beteen the vector and the main vectors'''
        angle = [0]*len(v.coords)
        for i in range(len(v.coords)):
           angle[i] = (acos(get_uv.coords[i])/180)*pi
        return angle
    def in_angle(v1,v2):
        '''Returns the angle between two vectors'''
        result = (v1.__mul__(v2))/(magnitude(v1)*magnitude(v2))
    def is_Collimated(v1,v2):
        return v1.__mul__(v2) == 0
    def is_perpendicular(v1,v2):
        '''works with only three dimensions'''
        return v1.cross_product.coords(v2) == [0,0,0]


            
        
        
        
        
        
