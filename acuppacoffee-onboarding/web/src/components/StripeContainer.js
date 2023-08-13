import React from 'react'
import { Elements } from "@stripe/react-stripe-js"
import { loadStripe } from "@stripe/stripe-js"

const PUBLIC_KEY = "pk_test_51JX8juB9Z2eW03LY87U1p5xkLXrUWamqk5W1Nj7w7vTTvjb33vKFkkIaDAUgWOs885djLSW5t1oP65Hzq0cNdN8M005xR2R9ji"

const stripeTestPromise = loadStripe(PUBLIC_KEY)
export default function StripeContainer() {
    return (
        <Elements stripe={stripeTestPromise}>
            <PaymentForm />
        </Elements>
    )
}
