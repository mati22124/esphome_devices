import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_FREQUENCY, CONF_ID

DEPENDENCIES = ['i2c']
MULTI_CONF = True

arduino_pe_ns = cg.esphome_ns.namespace('arduino_pe')
ArduinoPEOutput = arduino_pe_ns.class_('ArduinoPEOutput', cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(PCA9685Output),
    cv.Required(CONF_FREQUENCY): cv.All(cv.frequency,
                                        cv.Range(min=23.84, max=1525.88)),
}).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x40))


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_FREQUENCY])
    yield cg.register_component(var, config)
    yield i2c.register_i2c_device(var, config)
