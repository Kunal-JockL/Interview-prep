import axios from "axios";

export const getWeather = async (req, res) => {
    const {city} = req.params;
    try{
        const weatherData = await axios.get(process.env.WEATHER_URL, {
            params: {
                access_key: process.env.AK,
                query: city
            }
        });
        res.status(200).json({
            city,
            temperature: `${weatherData.data.current.temperature}°C`,
            humidity: `${weatherData.data.current.humidity}%`,
            wind_speed: `${weatherData.data.current.wind_speed} m/s`
        })
        console.log(weatherData.data)
    }catch(error){
        res.status(400).json(error.message)
        console.log(error.message)
    }
} 