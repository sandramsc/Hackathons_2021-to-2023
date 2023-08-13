import classNames from 'classnames';
import { forwardRef } from 'react';
export type InputSize = 'medium' | 'large';
export type InputType = 'text' | 'email' | 'password' | 'date' | 'datetime-local' | 'checkbox';

export type InputProps = {
    id: string;
    name: string;
    label: string;
    type?: InputType;
    size?: InputSize;
    placeholder: string;
    className?: string;
}

const sizeMap: { [key in InputSize]: string } = {
    medium: 'p-3 text-base',
    large: 'p-4 text-base',
};

export const Input: React.FC<InputProps> = forwardRef<HTMLInputElement, InputProps>(
    (
        {
            id,
            name,
            label,
            type = 'text',
            size = 'medium',
            className = '',
            placeholder,
            ...props
        },
        ref
    ) => {
        return (
            <div className="form-control w-full">
                <label className="label">
                    <span className="label-text">{label}</span>
                </label>
                <input
                    id={id}
                    ref={ref}
                    name={name}
                    type={type}
                    aria-label={label}
                    placeholder={placeholder}
                    autoComplete='off'
                    className={classNames([
                        'bg-transparent input input-bordered w-full',
                        sizeMap[size],
                        className,
                    ])}
                    {...props}
                />
            </div>
        );
    }
);

Input.displayName = "Input"