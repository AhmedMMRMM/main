from vector import Vector
from math import cos,pi
def torque_car(force,point):
	torque = force.cross_product(point)
	return torque
def torque_mag(force,length,inner_angle):
	torque = force*length*cos((inner_angle*180)/pi)
	return torque
def wrench(force,point):
	w = force*torque_car(force,point)
	w = w/force.magnitude()
	return w
def wrench_app_point(force,point):
	p = force.cross_product(torque_car(force,point))
	p = p*(1/((force.magnitude())**2))
	return p
def pitch(force,point):
	w = force*torque_car(force,point)
	w = w*(1/force.magnitude()**2)
	return w
